from polyfactory.factories.pydantic_factory import ModelFactory
from app.domain.models.score import Score

class PersonFactory(ModelFactory[Score]): ...