from django.core.management.base import BaseCommand, CommandParser
import requests
import logging
from app.settings import BAD_REQUEST


class Command(BaseCommand):
    help = "api command"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("parent_id", nargs=1, type=int)
        parser.add_argument("child_ids", nargs="+", type=int)

    def handle(self, *args, **options):
    
        print(options.get("parent_id"))
        print(options.get("child_ids"))
        logger = logging.getLogger(__name__.split(".").pop())
        
        response = requests.get("http://api:10001/test/api")
        
        # if response.status_code == BAD_REQUEST:
        #     logger.warning("bad request")
        
        