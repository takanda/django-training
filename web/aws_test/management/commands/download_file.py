import os
from django.core.management.base import BaseCommand, CommandParser
from aws_test.config import client, AWS_STORAGE_BUCKET_NAME


class Command(BaseCommand):
    help = "s3 file download command"

    def add_arguments(self, parser: CommandParser) -> None:
        pass

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(__file__), 'received_helloS3.txt')
        response = client.download_file(AWS_STORAGE_BUCKET_NAME, "helloS3.hxt", file_path)
        print(response)
