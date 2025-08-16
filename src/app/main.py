from fastapi import FastAPI
from .api.routes import router as api_router

app = FastAPI(title="Gen-AI-Assignment-22btrcb041")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")
