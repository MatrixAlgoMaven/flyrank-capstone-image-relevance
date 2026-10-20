import pytest
from pydantic import ValidationError

from src.app.schemas import ImageMetadata
from src.app.services.metadata_service import validate_image_metadata


def test_valid_image_metadata():
    metadata = ImageMetadata(
        subject="red fox",
        category="animal",
        attributes=["red fur", "pointed ears"],
        caption="A red fox standing in grass",
        confidence=0.95,
    )

    assert metadata.subject == "red fox"
    assert metadata.confidence == 0.95


def test_confidence_above_one_is_rejected():
    with pytest.raises(ValidationError):
        ImageMetadata(
            subject="red fox",
            category="animal",
            attributes=["red fur"],
            caption="A fox in grass",
            confidence=1.5,
        )

def test_empty_subject_is_rejected():
    with pytest.raises(ValidationError):
        ImageMetadata(
            subject="",
            category="animal",
            attributes=["red fur"],
            caption="A fox in grass",
            confidence=0.9,
        )


def test_empty_caption_is_rejected():
    with pytest.raises(ValidationError):
        ImageMetadata(
            subject="red fox",
            category="animal",
            attributes=["red fur"],
            caption="",
            confidence=0.9,
        )

def test_metadata_service_rejects_invalid_confidence():
    data = {
        "subject": "red fox",
        "category": "animal",
        "attributes": ["red fur"],
        "caption": "A fox in grass",
        "confidence": 1.5,
    }

    with pytest.raises(ValidationError):
        validate_image_metadata(data)