from fastapi import APIRouter

from core.dependencies import get_token_header
from schemas.scrape import ProductResponse, ScrapeRequest

from fastapi import Depends
from typing import List

from utils.scraper import ScrapeFileDBWithPrintNotifier

router = APIRouter()


@router.post("/", response_model=List[ProductResponse])
def scrape_products(request: ScrapeRequest):
    scrape_obj = ScrapeFileDBWithPrintNotifier()
    return scrape_obj.scrape_data_save_and_notify(num_pages=request.num_pages, proxy=request.proxy)
