import os
from django.core.management.base import BaseCommand, CommandParser
from aws_test.config import client, AWS_STORAGE_BUCKET_NAME
from app.settings import BASE_DIR


class Command(BaseCommand):
    help = "s3 file upload command"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("filename", nargs=1, type=str)

    def handle(self, *args, **options):
        filename = options.get("filename").pop()
        file_dir = os.path.join(BASE_DIR, "csv_file")
        file_path = os.path.join(file_dir, filename)
        
        client.upload_file(file_path, AWS_STORAGE_BUCKET_NAME, file_path)
