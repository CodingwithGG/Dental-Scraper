from fastapi import APIRouter

from apis.v1 import scrape

api_router = APIRouter()
api_router.include_router(scrape.router, prefix="/v1/scrape")


