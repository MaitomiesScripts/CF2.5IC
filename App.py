import os, sys
from PIL import Image

class App():
    def __init__(self):
        ImagePath = sys.argv[1]
        
        if self.ImageCheck(ImagePath):
            self.Convert(ImagePath)

    def ImageCheck(self, Path: str):
        AllowedExtensions = [".png", ".jpg", ".ico"]

        for FileExt in AllowedExtensions:
            if str.find(Path, FileExt):
                return True

        return False

    def Convert(self, Path: str):
        SIZES = [256, 128, 48, 32, 16]
        ImageMem = Image.open(Path)
        for Size in SIZES:
            Saveable = ImageMem.resize((Size, Size))
            Saveable.save(f"{os.path.basename(Path)}_{Size}_x_{Size}.png")


if __name__ == "__main__":
    App()