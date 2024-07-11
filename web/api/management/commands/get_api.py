import logging
from django.core.management.base import BaseCommand, CommandParser
from app.settings import API
from api.utils import RequestHandler


logger = logging.getLogger(API)

class Command(BaseCommand):
    help = "get api command"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("parent_id", nargs=1, type=int)
        parser.add_argument("child_id", nargs="+", type=int)
        
    def handle(self, *args, **options):
        """
            ・200は成功
            ・4xxはリトライ0（ただし409エラーの場合は成功とみなす）
            ・5xxはリトライ5（Exponential BackOff）
        """

        s = RequestHandler(retry={"count": 2})
        try:
            response = s.get("http://api:10001/test/api/500/bad_request")
            print("response", response.status_code)
        except AttributeError as e:
            print(e)
            return
