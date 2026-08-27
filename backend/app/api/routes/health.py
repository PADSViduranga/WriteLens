from fastapi import APIRouter

from app.core.config import settings


router = APIRouter(
    prefix="/api",
    tags=["Health"],
)


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": f"{settings.app_name} API",
        "environment": settings.app_env,
    }