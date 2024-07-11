from django.core.management.base import BaseCommand, CommandParser
from urllib3.util import Retry
import requests
from requests.adapters import HTTPAdapter
import logging
from app.settings import (STATUS_OK, STATUS_CREATED, STATUS_BAD_REQUEST, STATUS_UNAUTHORIZED,
                          STATUS_METHOD_NOT_ALLOWED, STATUS_CONFLICT, STATUS_TIMEOUT,
                          STATUS_SERVER_ERROR, STATUS_SERVER_UNAVAILABLE)


logger = logging.getLogger(__name__.split(".").pop().split("_").pop())

class Command(BaseCommand):
    help = "first api command"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("parent_id", nargs=1, type=int)
        parser.add_argument("child_ids", nargs="+", type=int)
        
    def handle(self, *args, **options):
        """
            ・200は成功
            ・4xxはリトライ0（ただし409エラーの場合は成功とみなす）
            ・5xxはリトライ5（Exponential BackOff）
        """

        s = requests.Session()
        s.headers.update({"Content-Type": "application/json"})
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500])
        s.mount('http://', LoggingHTTPAdapter(max_retries=retries))
        try:
            response = s.get("http://api:10001/test/api/400/bad_request")
            print("response", response)
        except AttributeError as e:
            print(e)
            return
        
        if response.status_code == STATUS_OK or response.status_code == STATUS_CONFLICT:
            print("success!", response.status_code)
            return

        if response.status_code >= STATUS_BAD_REQUEST and response.status_code < STATUS_SERVER_ERROR:
            logger.warning(response.json().pop())

class LoggingHTTPAdapter(HTTPAdapter):
    def send(self, request, **kwargs):
        try:
            response = super().send(request, **kwargs)
            if response.status_code in [400, 500, 502, 503, 504]:
                logger.warning(f'Request to {request.url} failed with status code {response.status_code}')
            return response
        except requests.exceptions.RetryError as e:
            logger.warning(f'RetryError for request to {request.url}: {e}')
            return
        except requests.exceptions.RequestException as e:
            logger.warning(f'Request to {request.url} failed with exception: {e}')
            return
        except Exception as e:
            logger.error(f'Unexpected error for request to {request.url}: {e}')
            return