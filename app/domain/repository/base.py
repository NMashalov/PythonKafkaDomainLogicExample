from typing import Generic, TypeVar

from app.core.engine.producer import ProducerFactory

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, producer: ProducerFactory):
        pass


