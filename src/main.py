import os
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in the .env file.")
print("✅ Environment variables loaded successfully.")

app = FastAPI()



if __name__ == "__main__":
    uvicorn.run("src:app", host="localhost", port=8000, reload=True)