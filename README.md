
# AI Image Understanding & Content Matching Engine

A Python backend that analyzes an image library, generates structured image metadata, and recommends relevant images for blog posts using semantic similarity and mismatch protection.

> **Status:** In progress - core functionality and evaluation are not yet complete.

## Problem

Choosing images for blog posts manually can be time-consuming. A similarity-based system can also make unsafe recommendations, such as matching a fox article with a wolf image.

This project aims to rank relevant images, explain its decisions, and reject uncertain or incompatible matches.

## Planned Features

- Structured image metadata using a vision model
- Semantic matching between image descriptions and blog posts
- Category and confidence-based mismatch guard
- Background processing with retries and progress tracking
- AI-call logging and cost controls
- API endpoints for recommendations and human review
- Evaluation using labelled examples and top-1 precision

## Planned Technology

- Python and FastAPI
- Google Gemini API
- Pydantic
- PostgreSQL and SQLAlchemy
- Alembic database migrations
- Pytest

## Dataset and Evaluation

The initial target is approximately 50 licensed-free images across at least four categories, with at least 10 labelled blog posts.

The primary evaluation metric will be top-1 precision. Dataset counts and measured results will be added after the evaluation pipeline is implemented.

## Setup

Requirements: Python 3.13, Git, and PostgreSQL.

1. Clone this repository.
2. Create and activate a virtual environment.
3. Install dependencies from `requirements.txt`.
4. Copy `.env.example` to `.env` and configure your local settings.
5. Set up the PostgreSQL database and run migrations.
6. Start the API using Uvicorn.

Detailed, verified commands will be added as implementation progresses.

## Project Design

See [DESIGN.md](DESIGN.md) for the architecture, data model, API plan, mismatch guard, and evaluation strategy.

## Security

- Secrets belong in `.env`, which must never be committed.
- `.env.example` contains placeholders only.
- API keys must not appear in logs or source code.

## License

MIT — see [LICENSE](LICENSE).
