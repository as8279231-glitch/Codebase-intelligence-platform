from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="Codebase Intelligence Platform",
    description="AI-powered platform for understanding software repositories",
    version="0.1.0"
)

# Allow React frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

app.mount(
    "/generated_reports",
    StaticFiles(directory="generated_reports"),
    name="generated_reports",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Codebase Intelligence Platform!",
        "status": "Backend is running successfully 🚀"
    }