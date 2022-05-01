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


def get_score(url=""):
    response = {url: []}
    for index, img in enumerate(images):
        basic_info = classifier.classify(str(img))
        for k, _ in basic_info.items():
            basic_score = basic_info[k]["safe"]
        detailed_info = detector.detect(str(img))
        response[url].append(
            {index: {"basic_score": basic_score, "detailed_score": detailed_info}}
        )
        Path(img).unlink()

    return response
