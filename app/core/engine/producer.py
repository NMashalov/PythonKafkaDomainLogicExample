from typing import Iterator
from kafka import KafkaProducer

from app.core.engine.settings import ProduceSettings


class ProducerFactory:
    def __init__(self, settings: ProduceSettings):
        self.settings = settings
        self.producer = KafkaProducer(
            bootstrap_servers=settings.bootstrap_servers,
            security_protocol=settings.security_protocol,
            sasl_mechanism=settings.sasl_mechanism,
            sasl_plain_username=settings.username,
            sasl_plain_password=settings.password,
        )

    def __enter__(self):
        return self.producer

    def __exit__(self):
        self.producer.flush()
        self.producer.close()
