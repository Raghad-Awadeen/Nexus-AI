
from fastapi import FastAPI

app = FastAPI(
    title="Nexus AI",
    description="Enterprise Knowledge Assistant API",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "project": "Nexus AI",
        "status": "running",
        "message": "Welcome to Nexus AI"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
