import logging
import requests
import json
from requests.exceptions import HTTPError
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from app.settings import (STATUS_OK, STATUS_CREATED, STATUS_BAD_REQUEST, STATUS_UNAUTHORIZED,
                          STATUS_METHOD_NOT_ALLOWED, STATUS_CONFLICT, STATUS_TIMEOUT,
                          STATUS_SERVER_ERROR, STATUS_SERVER_UNAVAILABLE, API_LOG_NAME, CONTENT_TYPE)

logger = logging.getLogger(API_LOG_NAME)


class LoggingHTTPAdapter(HTTPAdapter):
    def send(self, request, **kwargs):
        try:
            response = super().send(request, **kwargs)
            response.raise_for_status()
            return response
        except HTTPError as e:
            error_msg = e.response.content.decode("utf-8")
            logger.error(json.loads(error_msg).get("detail"))
        except requests.exceptions.RequestException as e:
            logger.warning(
                f'Request to {request.url} failed with exception: {e}')
            return
        except Exception as e:
            logger.error(f'Unexpected error for request to {request.url}: {e}')
            return

class RequestHandler():

    def __init__(self, header={}, retry={}) -> None:
        self.s = requests.Session()
        self.s.headers.update({"Content-Type": header.get("content_type",
                              CONTENT_TYPE), "Authorization": header.get("authorization", None)})
        self.retries = Retry(total=retry.get("count", 5), backoff_factor=retry.get("backoff_factor", 1), status_forcelist=retry.get(
                            "status_forcelist", [STATUS_TIMEOUT, STATUS_SERVER_ERROR, STATUS_SERVER_UNAVAILABLE]),
                             raise_on_status=False)
        self.s.mount('http://', LoggingHTTPAdapter(max_retries=self.retries))
        
    def get(self, url):
        return self.s.get(url)

    def post(self, url, json):
        return self.s.post(url, json=json)
