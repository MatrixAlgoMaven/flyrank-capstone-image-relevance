from fastapi import FastAPI

app = FastAPI(
    title="AI Image Understanding & Content Matching Engine",
    description="A backend for understanding images and matching them to blog posts.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}