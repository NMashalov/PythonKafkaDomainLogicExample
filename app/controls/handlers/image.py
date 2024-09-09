from pathlib import Path

from app.controls.handlers.base import BaseHandler
from app.domain.repository.image import ImageRepository
from app.core.io.image import ImageFolder


class ImageHandler(BaseHandler):
    def __init__(self, image_repository: ImageRepository):
        self.image_repository = image_repository

    def produce_from_folder(self, image_folder_path: Path, annotation_file_path: Path):
        self.image_repository.produce_from_folder(
            image_folder=ImageFolder(image_folder=image_folder_path)
        )
