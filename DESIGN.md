# AI Image Understanding & Content Matching Engine

## 1. Problem Statement

Build a Python backend that understands a small library of images, automatically tags them, and recommends suitable images for blog posts. The system must reject incorrect or uncertain recommendations instead of returning a misleading match.

## 2. Scope and Dataset

The initial corpus will contain approximately 50 licensed-free images across at least four categories. Example animal categories include foxes, wolves, dogs, bears, and deer. At least 10 blog posts will form a manually labelled evaluation dataset.

## 3. Technology Stack

- Python 3.13 and FastAPI
- Gemini Flash for image understanding and Gemini embeddings, subject to free-tier availability
- Pydantic for schema validation
- PostgreSQL for persistent storage
- Background processing with retries and progress tracking
- Environment variables for secrets

## 4. Data Model

- **Image:** ID, file path, source, category, processing status
- **ImageMetadata:** subject, category, attributes, caption, confidence
- **Embedding:** associated image or post ID and vector values
- **Post:** ID, title, body and embedding
- **Suggestion:** post ID, image ID, similarity score, guard decision and explanation
- **Review:** suggestion ID, decision and review timestamp
- **AICallLog:** operation, associated record, status, attempt count and cost

## 5. API Surface

- `GET /health` — service health
- `GET /posts/{post_id}/images` — ranked image recommendations
- `POST /images/process` — request batch processing
- `GET /jobs/{job_id}` — inspect job status and progress
- `GET /suggestions/{suggestion_id}` — inspect a suggestion and its explanation
- `POST /suggestions/{suggestion_id}/review` — approve or reject a suggestion

Exact request and response schemas will be finalized during implementation.

## 6. Matching and Mismatch Guard

Generate embeddings for image captions and post content, then rank images by cosine similarity. The guard will combine semantic similarity, validated image categories, and model confidence. It will reject category mismatches, flag low-confidence classifications, and return “no confident match” when no candidate passes the configured thresholds. Thresholds will be evaluated against labelled examples rather than selected solely by intuition.

## 7. Architecture

Image corpus → background vision job → validated metadata → image embeddings → database.

Blog post → text embedding → similarity ranking → mismatch guard → explained suggestion or safe rejection → human review.

## 8. Quality and Evaluation

Tests will cover schema validation, retry behaviour, mismatch rejection and API input validation. An evaluation script will calculate top-1 precision on at least 10 labelled posts. Every AI call will be logged for cost tracking.

## 9. Explicit Non-Goal

This project will not build a public-facing image marketplace or a full content-management system. The focus is a small, reproducible backend that demonstrates reliable image understanding and safe semantic matching.

## 10. Limitations

Model-generated metadata may be incorrect. Similarity scores are not calibrated probabilities. Results depend on the image corpus, model availability, confidence thresholds and labelled evaluation data. Uncertain cases must be flagged or rejected.