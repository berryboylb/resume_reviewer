from fastapi import APIRouter, status,File, UploadFile, HTTPException
from src.models.evaluation import Evaluation
from src.resume_parser import ResumeParser
from src.ai_evaluator import AgentActions
from src.constant import JOB_DESCRIPTION
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
import asyncio

router = APIRouter(prefix="/evaluations", tags=["Evaluations"])

@router.post("/")
async def test():
    return {"msg": "hello"}

@router.get("/")
async def evaluate(body: Evaluation):
    try:
        parser = ResumeParser()
        text = parser.extract_text(body.file_path)
        
        actions = AgentActions()

        # async def response_generator() -> AsyncGenerator[str, None]:
        #     async for chunk in actions.rank_resume(text, JOB_DESCRIPTION):
        #         yield chunk
        #         await asyncio.sleep(0)  # Give control back to the event loop
        
        return StreamingResponse(actions.rank_resume(text, JOB_DESCRIPTION), media_type='text/event-stream')
        # return StreamingResponse(actions.fake_data_streamer(), media_type='text/event-stream')

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Evaluation failed: {str(e)}")