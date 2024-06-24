import redis
import json
from typing import Optional


class Cache:
    def __init__(self, redis_url: str = "redis://localhost"):
        self.redis = redis.StrictRedis.from_url(redis_url)

    def get_product(self, title: str) -> Optional[dict]:
        product = self.redis.get(title)
        if product:
            return json.loads(product)
        return None

    def set_product(self, title: str, product: dict):
        self.redis.set(title, json.dumps(product))
