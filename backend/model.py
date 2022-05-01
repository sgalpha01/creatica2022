from pydantic import BaseModel


class NSFW_score_image(BaseModel):
    basic_score: int
    detailed_score: list


class NSFW_score(BaseModel):
    url: str
    description: NSFW_score_image
