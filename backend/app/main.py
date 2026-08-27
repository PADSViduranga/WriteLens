from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes.analysis import router as analysis_router
from app.api.routes.health import router as health_router
from app.core.config import settings
from app.core.exceptions import WriteLensException


app = FastAPI(
    title=f"{settings.app_name} API",
    description="Backend API for the WriteLens writing analysis platform.",
    version="0.1.0",
)


@app.exception_handler(WriteLensException)
async def writelens_exception_handler(
    request: Request,
    exc: WriteLensException,
):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
            }
        },
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


app.include_router(health_router)
app.include_router(analysis_router)