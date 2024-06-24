from typing import Optional

from pydantic.main import BaseModel


class ScrapeRequest(BaseModel):
    num_pages: int
    proxy: Optional[str] = None


class ProductResponse(BaseModel):
    title: str
    price: float
    image_url: str
