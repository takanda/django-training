import os
import csv
import random
import datetime
from django.core.management.base import BaseCommand, CommandParser
from app.settings import BASE_DIR

class Command(BaseCommand):
    help = "create csv file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("row_count", nargs=1, type=int)

    def handle(self, *args, **options):
        row_count = options.get("row_count").pop()
        today = datetime.date.today()
        
        file_dir = os.path.join(BASE_DIR, "csv_file")
        file = "test" + str(today.strftime("%Y%m%d")) + ".csv"
        file_path = os.path.join(file_dir, file)
        columns = ["id", "birthday"]    
    
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(columns)
        
        row_list = []
        for i in range(1, row_count+1):
            birthday = today - datetime.timedelta(days=random.randint(1, 365*50))
            row_list.append([i, birthday])
            
        with open(file_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(row_list)
