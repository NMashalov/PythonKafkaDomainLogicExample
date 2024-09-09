from typer import Typer

from app.controls.router.base import BaseRouter
from app.controls.handlers.produce import ProduceHandler


class ProduceRouter(BaseRouter):
    def __init__(self, handler: ProduceHandler):
        self.producer_handler = handler

    def prepare_router(self):
        producer = Typer("Producer")
        producer.command("from csv")(self.producer_handler.from_csv)
        return producer
