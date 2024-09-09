from pathlib import Path


class ImageFolder:
    def __init__(self, image_folder: Path):
        self.image_folder = image_folder

    def images_iterator(
        self,
    ):
        for image_path in self.image_folder.glob("*"):
            with image_path.open("r") as image:
                yield image.read()
