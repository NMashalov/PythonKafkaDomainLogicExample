from pathlib import Path
from csv import DictReader

class CsvRepo:
    def __init__(self, csv_path:  Path):
        self.csv_path = csv_path

    def iterator(self):
        with self.csv_path.open('r') as csv_file:
            for row in DictReader(csv_file):
                yield row
    
    def dedub_iterator(self):
        dedub_set = set()
        with self.csv_path.open('r') as csv_file:
            for row in DictReader(csv_file):
                if row not in dedub_set:
                    yield row
                    dedub_set.add(row)
