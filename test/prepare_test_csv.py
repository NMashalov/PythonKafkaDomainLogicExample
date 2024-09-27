from csv import DictWriter

from polyfactory.factories.pydantic_factory import ModelFactory
from pydantic import BaseModel

from app.domain.models.score import ScoreInput



class CsvInput(BaseModel):
    ...

class ScoreFactory(ModelFactory[CsvInput]): ...


def prepare_csv(csv_name: str, number_of_rows: int =100):
    with open(csv_name,'w') as f:
        writer = DictWriter(f)
        writer.writeheader()
        for row in ScoreFactory.batch(size=number_of_rows):
            writer.writerow(row.model_dump())
