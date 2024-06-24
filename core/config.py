import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path('.') / 'local.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Dental Scraper"
    PROJECT_VERSION: str = "1.0.0"
    SITE_URL: str = "https://dentalstall.com/shop"
    FILE_PATH: str = "products.json"
    AUTH_TOKEN: str = ""


settings = Settings()
