from django.core.management.base import BaseCommand
import requests
import logging
from app.settings import BAD_REQUEST


class Command(BaseCommand):
    help = "api command"

    def handle(self, *args, **options):
        logger = logging.getLogger(__name__.split(".").pop())
        
        response = requests.get("http://api:10001/test/api")
        
        if response.status_code == BAD_REQUEST:
            logger.warning("bad request")
        
        