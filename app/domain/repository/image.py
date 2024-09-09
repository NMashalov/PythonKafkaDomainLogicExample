from app.core.engine.producer import ProducerFactory
from app.domain.models.image import Image
from app.core.io.image import ImageFolder
from app.domain.repository.base import BaseRepository


class ImageRepository(BaseRepository):
    def __init__(self, producer_factory: ProducerFactory):
        self.producer_factory = producer_factory

    def produce_from_folder(self, image_folder: ImageFolder):
        for image in image_folder.images_iterator():
            with self.producer_factory as producer:
                producer.send()
