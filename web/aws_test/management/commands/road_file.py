import os
from django.core.management.base import BaseCommand, CommandParser
from aws_test.config import client, AWS_STORAGE_BUCKET_NAME
from app.settings import BASE_DIR


class Command(BaseCommand):
    help = "road s3 file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("filename", nargs=1, type=str)

    def handle(self, *args, **options):
        filename = options.get("filename").pop()
        file_dir = os.path.join(BASE_DIR, "csv_file")
        file_path = os.path.join(file_dir, filename)
        
        res = client.get_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=file_path)        
        content_list = res["Body"].read().decode("utf-8").splitlines()
        
        # delete header
        del content_list[0]
        
        for content in content_list:
            user_id, birthday = content.split(",")
            print(user_id)
            print(birthday)
