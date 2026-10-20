from fastapi.testclient import TestClient
from io import BytesIO

import pytest
from PIL import Image
from src.app.main import app

client = TestClient(app)
from src.app.services.image_service import validate_image_file


def create_test_image() -> bytes:
    """Create a tiny PNG image in memory."""
    buffer = BytesIO()

    image = Image.new("RGB", (10, 10), color="red")
    image.save(buffer, format="PNG")

    return buffer.getvalue()


def test_valid_png_is_accepted():
    content = create_test_image()

    result = validate_image_file("test.png", content)

    assert result["filename"] == "test.png"
    assert result["format"] == "PNG"
    assert result["size_bytes"] == len(content)


def test_empty_file_is_rejected():
    with pytest.raises(ValueError, match="empty"):
        validate_image_file("empty.png", b"")


def test_invalid_image_is_rejected():
    with pytest.raises(ValueError, match="valid image"):
        validate_image_file("fake.png", b"this is not an image")


def test_oversized_file_is_rejected():
    content = b"x" * (5 * 1024 * 1024 + 1)

    with pytest.raises(ValueError, match="5 MB"):
        validate_image_file("large.png", content)


def test_upload_valid_png():
    content = create_test_image()

    response = client.post(
        "/images/validate",
        files={"file": ("test.png", content, "image/png")},
    )

    assert response.status_code == 200
    assert response.json()["format"] == "PNG"
    assert response.json()["filename"] == "test.png"


def test_upload_invalid_image():
    response = client.post(
        "/images/validate",
        files={"file": ("fake.png", b"not an image", "image/png")},
    )

    assert response.status_code == 400
    assert "valid image" in response.json()["detail"]
