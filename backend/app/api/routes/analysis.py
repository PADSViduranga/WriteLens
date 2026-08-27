from fastapi import APIRouter

from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.services.analysis_service import analysis_service


router = APIRouter(
    prefix="/api/analysis",
    tags=["Analysis"],
)


@router.post("", response_model=AnalysisResponse)
async def analyze_text(request: AnalysisRequest):
    result = await analysis_service.analyze(request.text)

    return AnalysisResponse(**result)