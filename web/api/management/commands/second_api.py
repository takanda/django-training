from django.core.management.base import BaseCommand, CommandParser
import requests
import logging
from app.settings import (STATUS_OK, STATUS_CREATED, STATUS_BAD_REQUEST, STATUS_UNAUTHORIZED,
                          STATUS_METHOD_NOT_ALLOWED, STATUS_CONFLICT, STATUS_TIMEOUT, 
                          STATUS_SERVER_ERROR, STATUS_SERVER_UNAVAILABLE)

class Command(BaseCommand):
    help = "second api command"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("parent_id", nargs=1, type=int)

    def handle(self, *args, **options):
        """
            ・200は成功
            ・4xxはリトライ0（ただし409エラーの場合は成功とみなす）
            ・5xxはリトライ5（Exponential BackOff）
        """

        logger = logging.getLogger(__name__.split(".").pop().split("_").pop())

        response = requests.get("http://api:10001/test/api/400/bad_request")
        if response.status_code == STATUS_OK or response.status_code == STATUS_CONFLICT:
            print("success!", response.status_code)
            return

        if response.status_code >= STATUS_BAD_REQUEST and response.status_code < STATUS_SERVER_ERROR:
            logger.warning(response.json().pop())
