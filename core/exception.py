from fastapi import status
from fastapi.exceptions import HTTPException


class ApiException(HTTPException):
    extra = None
    error_code = None
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'The server encounters an unexpected exception while trying to process the request.'
    errors = []
    rollback_transaction = True

    def __init__(self, message: str = None, status_code: int = None) -> None:
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        super().__init__(status_code, message)
