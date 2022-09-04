from fastapi import APIRouter

from app.api.api_v1.endpoints import templates

api_router = APIRouter()
api_router.include_router(templates.router, prefix="/templates", tags=["templates"])
