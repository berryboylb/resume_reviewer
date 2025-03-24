from fastapi import APIRouter, status,File, UploadFile, HTTPException
from typing import Union
from src.cloudinary import Cloudinary
import io
router = APIRouter(prefix="/upload", tags=["Upload"])

@router.get("/")
async def upload():
    return {"msg": "hello"}

@router.post("/")
async def upload(file: UploadFile = File(...)):
    """Uploads a file to Cloudinary and returns the URL."""
    
    try:
        # Convert UploadFile to a file-like object
        file_bytes = await file.read()
        file_stream = io.BytesIO(file_bytes)
        
        cloudinary = Cloudinary()

        # Upload to Cloudinary
        res =  cloudinary.upload(file_stream, "resume")

        return {"res": res}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}