import logging
from django.core.management.base import BaseCommand, CommandParser
from api.config import client, AWS_STORAGE_BUCKET_NAME


class Command(BaseCommand):
    help = "s3 file upload command"

    def add_arguments(self, parser: CommandParser) -> None:
        pass

    def handle(self, *args, **options):
        response = client.get_bucket_location(Bucket=AWS_STORAGE_BUCKET_NAME)
        print(response)
