from typer import Typer

from app.controls.router.base import BaseRouter


class Cli:
    def __init__(self, routers: list[BaseRouter]):
        self.app = Typer(name="Kafka client for batch upload of image.")
        for router in routers:
            self.app.add_typer(router.prepare_router())

    def run(self):
        self.app()
