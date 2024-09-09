from typing import Iterator
from kafka import KafkaProducer

from app.core.engine.settings import ProduceSettings


class ProducerFactory:
    def __init__(self, settings: ProduceSettings):
        self.settings = settings
        self.producer = KafkaProducer(bootstrap_servers="localhost:1234")

    def __enter__(self):
        return self.producer

    def __exit__(self):
        self.producer.flush()
        self.producer.close()
