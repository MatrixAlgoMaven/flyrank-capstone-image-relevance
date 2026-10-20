from pydantic import BaseModel, Field


class ImageMetadata(BaseModel):
    subject: str = Field(min_length=1)
    category: str = Field(min_length=1)
    attributes: list[str]
    caption: str = Field(min_length=1)
    confidence: float = Field(ge=0.0, le=1.0)