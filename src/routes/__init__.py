from fastapi import APIRouter
router = APIRouter(prefix="/v1")

from src.routes.upload import router as upload_router

router.include_router(upload_router)