from app.cli import Cli
from app.controls.router.score import ScoreRouter
from app.controls.handlers.score import ScoreHandler
from app.domain.repository.score import ScoreRepository
from app.core.engine.producer import ProducerFactory
from app.core.engine.settings import ProduceSettings


def prepare_app():
    return Cli(
        routers=[
            ScoreRouter(
                handler=ScoreHandler(
                    score_repository=ScoreRepository(
                        producer=ProducerFactory(ProduceSettings())
                    )
                )
            )
        ]
    )
