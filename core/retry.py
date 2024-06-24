import logging
import time

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1):
    """
    Decorator function that retries executing a function multiple times in case of exceptions.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    attempts += 1
                    # Log the exception and attempt information
                    logger.warning(f"Function {func.__name__} raised an exception: {e}")
                    logger.warning(f"Attempt {attempts}/{max_attempts} failed. Retrying in {delay} seconds.")
                    time.sleep(delay)
            # If all attempts fail, log the failure and raise an exception
            logger.exception(f"Sync function {func.__name__} failed after {max_attempts} attempts.")
            raise Exception(f"{func.__name__} failed after {max_attempts} attempts.")


        return wrapper

    return decorator