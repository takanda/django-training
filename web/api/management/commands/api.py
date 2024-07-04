from django.core.management.base import BaseCommand
import requests
import time

class Command(BaseCommand):
    help = "api command"

    def handle(self, *args, **options):
        time.sleep(5)
        response = requests.get("http://api:10001/test/api")
        print(response.text)