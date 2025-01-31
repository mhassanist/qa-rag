import os
from fastapi import FastAPI, APIRouter

base_router = APIRouter(
    prefix="/api/v1",
    tags=["base"],
)

@base_router.get("/")
async def read_root():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {"app_name": app_name, "app_version": app_version}
