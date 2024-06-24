from fastapi import APIRouter

from core.dependencies import get_token_header
from schemas.scrape import ProductResponse, ScrapeRequest

from fastapi import Depends
from typing import List

router = APIRouter()


@router.post("/scrape", response_model=List[ProductResponse], dependencies=[Depends(get_token_header)])
async def scrape_products(request: ScrapeRequest):
    """"""
