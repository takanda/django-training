import logging
import os
from django.core.management.base import BaseCommand, CommandParser
from api.config import client, AWS_STORAGE_BUCKET_NAME


class Command(BaseCommand):
    help = "s3 file upload command"

    def add_arguments(self, parser: CommandParser) -> None:
        pass

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(__file__), 'helloS3.txt')
        response = client.upload_file(file_path, AWS_STORAGE_BUCKET_NAME, "helloS3.hxt")
        print(response)
