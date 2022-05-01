from pathlib import Path, PurePath

from nudenet import NudeClassifier, NudeDetector

workdir = Path(__file__).resolve().parent
imgdir = PurePath.joinpath(workdir, ".image_cache")
Path(imgdir).mkdir(exist_ok=True)
images = [p for p in imgdir.iterdir() if p.is_file()]

# initialize classifier
classifier = NudeClassifier()

# initialize detector
detector = NudeDetector()


def results():
    for index, img in enumerate(images, 1):
        print(f"For image {index}:")
        print(classifier.classify(str(img)))
        print(detector.detect(str(img)))
        print()
