from abc import ABC, abstractmethod
from typing import List

from core.notifier import PrintNotifier, NotifierInterface
from utils.save_product import FileDatabase, DatabaseInterface


class Product:
    def __init__(self, title: str, price: float, image_url: str):
        self.title = title
        self.price = price
        self.image_url = image_url


class Scraper:
    def __init__(self):
        """"""

    def scrape_page(self, page_number: int) -> List[Product]:
        """"""

    def scrape(self, num_pages: int) -> List[Product]:
        """"""


class BaseScrapeDBNotifer(ABC):
    def __init__(self):
        self.database = DatabaseInterface
        self.notifier = NotifierInterface

    @abstractmethod
    def scrape_data_save_and_notify(self):
        """"""


class ScrapeFileDBWithPrintNotifier():

    def __init__(self):
        self.database = FileDatabase
        self.notifier = PrintNotifier

    def scrape_data_save_and_notify(self):
        """"""
