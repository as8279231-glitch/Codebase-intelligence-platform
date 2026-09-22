from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Codebase Intelligence Platform",
    description="AI-powered platform for understanding software repositories",
    version="0.1.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Codebase Intelligence Platform!",
        "status": "Backend is running successfully 🚀"
    }