from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health", summary="Health Check")
async def health_check():
    return JSONResponse({"status": "ok", "message": "API is healthy"})
