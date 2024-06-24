from fastapi import APIRouter, Depends
from typing import List
from core.dependencies import get_token_header
from schemas.scrape import ProductResponse, ScrapeRequest
from utils.scraper import ScrapeFileDBWithPrintNotifier

router = APIRouter()

@router.post("/", response_model=List[ProductResponse], dependencies=[Depends(get_token_header)])
def scrape_products(request: ScrapeRequest):
    """
    Endpoint to scrape products based on the provided request.
    """
    # Initialize the scraper object
    scrape_obj = ScrapeFileDBWithPrintNotifier()

    # Perform scraping and return results
    return scrape_obj.scrape_data_save_and_notify(num_pages=request.num_pages, proxy=request.proxy)
