import json
from abc import abstractmethod, ABC
from typing import List
import os

from core.config import settings


class DatabaseInterface(ABC):

    @abstractmethod
    def save_products(self, products: List[dict]):
        """"""

    @abstractmethod
    def load_products(self) -> List[dict]:
        """"""


class FileDatabase:
    def __init__(self):
        self.file_path = settings.FILE_PATH

    def save_products(self, products: List[dict]):
        with open(self.file_path, 'w') as f:
            json.dump(products, f, indent=4)

    def load_products(self) -> List[dict]:
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return []


class PostgresDatabase:
    def __init__(self):
        """"""

    def save_products(self, products: List[dict]):
        """can be used later on to save products into database"""

    def load_products(self, ):
        """can be used later on to load products from database"""
