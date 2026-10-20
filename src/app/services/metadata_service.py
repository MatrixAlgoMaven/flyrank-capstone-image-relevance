from ..schemas import ImageMetadata


def validate_image_metadata(data: dict) -> ImageMetadata:
    """Validate metadata generated for an image."""
    return ImageMetadata.model_validate(data)