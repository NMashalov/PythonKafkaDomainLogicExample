from typer import Typer

from app.controls.handlers.base import BaseHandler


class BaseRouter:
    def __init__(self, handler: BaseHandler):
        pass

    def prepare_router(self) -> Typer:
        pass
