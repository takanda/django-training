from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = "api command"

    def handle(self, *args, **options):
        response = requests.get("http://api:10001/test/api")
        return response.text