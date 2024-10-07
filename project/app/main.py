from fastapi import FastAPI, Depends
from app.config import get_settings, Settings
import os

app = FastAPI()

# class Settings(BaseSettings):
#     environment: str = "dev"
#     testing: bool = bool(0)


# def get_settings() -> BaseSettings:
#     log.info("Loading config settings from the environment...")
#     return Settings()

@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
