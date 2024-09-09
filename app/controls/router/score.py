from typer import Typer

from app.controls.router.base import BaseRouter
from app.controls.handlers.score import ScoreHandler


class ScoreRouter(BaseRouter):
    def __init__(self, handler: ScoreHandler):
        self.score_handler = handler

    def prepare_router(self):
        producer = Typer("Producer")
        producer.command("from csv")(self.score_handler.from_csv)
        return producer
