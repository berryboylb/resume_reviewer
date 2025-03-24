from fastapi import FastAPI, HTTPException, APIRouter
from src.routes import router
from src.functions.handlers import logger_exception_handler


app = FastAPI()
app.exception_handler(HTTPException)(logger_exception_handler)
# router = APIRouter(prefix="/v1")
app.include_router(router)