from typing import Iterator
from kafka import KafkaProducer

from app.core.engine.settings import ProduceSettings

class Producer:
    def __init__(self, settings: ProduceSettings):
        self.settings = settings
        self.producer = self.prepare_producer()
        
    def prepare_producer(self):
        return KafkaProducer(
            bootstrap_servers='localhost:1234'
        )

    def from_iterator(self, iterator: Iterator[str]):
        for item in iterator:
            self.producer.send(
                topic=self.topic,
                value=item
            )
        self.producer.flush()