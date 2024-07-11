import logging
from django.core.management.base import BaseCommand, CommandParser
from app.settings import API
from api.utils import RequestHandler


logger = logging.getLogger(API)

class Command(BaseCommand):
    help = "post api command"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("parent_id", nargs=1, type=int)
        parser.add_argument("child_id", nargs="+", type=int)
        
    def handle(self, *args, **options):
        """
            ・200は成功
            ・4xxはリトライ0（ただし409エラーの場合は成功とみなす）
            ・5xxはリトライ5（Exponential BackOff）
        """

        s = RequestHandler()
        body = {
            "parent_id": options["parent_id"],
            "child_id": [id for id in options["child_id"]]
        }
        
        try:
            response = s.post("http://api:10001/test/api/201/create", json=body)
            print("response", response)
        except AttributeError as e:
            print(e)
            return