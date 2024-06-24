from fastapi import Header

from core.config import settings
from core.exception import ApiException


def get_token_header(token: str = Header(...)):
    if token != settings.AUTH_TOKEN:
        raise ApiException(status_code=403, message="Invalid authentication token")
