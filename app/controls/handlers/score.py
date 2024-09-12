from pathlib import Path

from app.domain.models.score import ScoreType
from app.io.csv import CsvFile
from app.domain.repository.score import ScoreRepository


class ScoreHandler:
    def __init__(self, score_repository: ScoreRepository):
        self.score_repository = score_repository

    def from_csv(self, csv_path: Path, score_type: ScoreType = ScoreType.novice):
        self.score_repository.produce_from_csv(csv_file=CsvFile(csv_path=csv_path))
