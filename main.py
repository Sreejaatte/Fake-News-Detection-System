from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Fake News Detection API")

app.include_router(router, prefix="/api/v1")
