from io import BytesIO

from PIL import Image, UnidentifiedImageError


ALLOWED_FORMATS = {"JPEG", "PNG", "WEBP"}
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB


def validate_image_file(filename: str, content: bytes) -> dict:
    """Validate image size and actual image format."""
    if not content:
        raise ValueError("Image file is empty.")

    if len(content) > MAX_IMAGE_SIZE:
        raise ValueError("Image exceeds the 5 MB size limit.")

    try:
        with Image.open(BytesIO(content)) as image:
            image_format = image.format

            if image_format not in ALLOWED_FORMATS:
                raise ValueError("Only JPEG, PNG, and WebP images are allowed.")

            image.verify()

    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError("Uploaded file is not a valid image.") from exc

    return {
        "filename": filename,
        "format": image_format,
        "size_bytes": len(content),
    }