from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import ValidationError

from .schemas import ImageMetadata
from .services.metadata_service import validate_image_metadata
from .services.image_service import (
    MAX_IMAGE_SIZE,
    validate_image_file,
)

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

@app.post("/images/validate")
async def validate_uploaded_image(file: UploadFile = File(...)):
    try:
        content = await file.read(MAX_IMAGE_SIZE + 1)

        return validate_image_file(
            filename=file.filename or "unknown",
            content=content,
        )

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    finally:
        await file.close()