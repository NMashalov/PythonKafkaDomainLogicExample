from app.core.engine.producer import ProducerFactory
from app.core.io.csv import CsvFile

from app.domain.models.score import Score
from app.domain.repository.base import BaseRepository


class ScoreRepository(BaseRepository):
    def __init__(self, producer_factory: ProducerFactory):
        self.producer_factory = producer_factory

    def produce_from_csv(self, csv_file: CsvFile):
        with self.producer_factory as producer:
            for score_row in csv_file.iterator():
                score = Score.model_validate(score_row)
                producer.send(score)
