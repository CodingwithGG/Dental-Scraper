from abc import ABC, abstractmethod
from typing import List

import requests
from bs4 import BeautifulSoup

from core.cache import Cache
from core.config import settings
from core.notifier import PrintNotifier, NotifierInterface
from core.retry import retry
from utils.save_product import FileDatabase, DatabaseInterface


class Product:
    def __init__(self, title: str, price: float, image_url: str):
        self.title = title
        self.price = price
        self.image_url = image_url


class Scraper:
    def __init__(self, base_url: str, proxy: str = None):
        self.base_url = base_url
        self.proxy = proxy
        self.session = requests.Session()
        if proxy:
            self.session.proxies = {
                "http": proxy,
                "https": proxy,
            }

    @retry(max_attempts=3, delay=2)
    def scrape_page(self, page_number: int) -> List[Product]:
        url = f"{self.base_url}/page/{page_number}/"
        response = self.session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        products = []
        for product_element in soup.select('.product'):
            price_element = product_element.select_one('.price .woocommerce-Price-amount.amount bdi')
            image_element = product_element.select_one('.mf-product-thumbnail img')

            title = image_element['alt'] if image_element and 'alt' in image_element.attrs else 'N/A'
            price = float(
                price_element.get_text(strip=True).replace('₹', '').replace(',', '')) if price_element else 0.0
            image_url = image_element['data-lazy-src'] if image_element and 'data-lazy-src' in image_element.attrs else \
            image_element['src']

            products.append(Product(title, price, image_url))

        return products

    def scrape(self, num_pages: int) -> List[Product]:
        all_products = []
        for page in range(1, num_pages + 1):
            try:
                products = self.scrape_page(page)
                all_products.extend(products)
            except requests.RequestException as e:
                print(f"Failed to scrape page {page}: {e}")
        return all_products


class BaseScrapeDBNotifer(ABC):
    def __init__(self):
        self.database = DatabaseInterface
        self.notifier = NotifierInterface

    def scrape_data_save_and_notify(self, num_pages: int = 5, proxy: str | None = None):
        scraper = Scraper(settings.SITE_URL, proxy)
        scraped_products = scraper.scrape(num_pages)

        new_products = []
        for product in scraped_products:
            cached_product = Cache().get_product(product.title)
            if cached_product is None or cached_product['price'] != product.price:
                product_data = {
                    "title": product.title,
                    "price": product.price,
                    "image_url": product.image_url
                }
                Cache().set_product(product.title, product_data)
                new_products.append(product_data)
        if new_products:
            self.database().save_products(new_products)
        self.notifier().notify(message=f"Scraped and updated {len(new_products)} products.")

        return new_products


class ScrapeFileDBWithPrintNotifier(BaseScrapeDBNotifer):

    def __init__(self):
        self.database = FileDatabase
        self.notifier = PrintNotifier
