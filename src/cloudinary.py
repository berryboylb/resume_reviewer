import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv
import os
from src.constant import CLOUDINARY_PUBLIC_ID


load_dotenv()

class Cloudinary:
    def __init__(self):
        cloudinary.config( 
            cloud_name =  os.getenv("CLOUDINARY_CLOUD"), 
            api_key = os.getenv("CLOUDINARY_CLOUD_SECRET"), 
            api_secret = os.getenv("CLOUDINARY_CLOUD_KEY"), 
            secure=True
        )
    
    def upload(self, url: str, folder: str):
        response = cloudinary.uploader.upload(url, folder=folder, public_id=CLOUDINARY_PUBLIC_ID)
        print(f"this is the response: {response}")
        return response

