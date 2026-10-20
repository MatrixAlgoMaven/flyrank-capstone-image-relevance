from fastapi import FastAPI, HTTPException
from pydantic import ValidationError

from src.app.schemas import ImageMetadata
from src.app.services.metadata_service import validate_image_metadata

app = FastAPI(
    title="AI Image Understanding & Content Matching Engine",
    description="A backend for understanding images and matching them to blog posts.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/metadata/validate", response_model=ImageMetadata)
def validate_metadata(data: dict):
    try:
        return validate_image_metadata(data)
    except ValidationError as exc:
        raise HTTPException(status_code=422, detail=exc.errors()) from exc