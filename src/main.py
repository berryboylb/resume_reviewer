import os
import asyncio
from dotenv import load_dotenv
from resume_parser import extract_text
from ai_evaluator import rank_resume

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in the .env file.")

print("✅ Environment variables loaded successfully.")

JOB_DESCRIPTION = """Software Developer role requiring Python, AI, and Resume Screening experience."""

async def process_resumes():
    resumes = [f for f in os.listdir("data/") if f.endswith((".pdf", ".docx"))]
    results = []

    for resume in resumes:
        print(f"🔍 Processing {resume}...")
        text = extract_text(f"data/{resume}")
        score = await rank_resume(text, JOB_DESCRIPTION)  # ✅ Await async function
        results.append((resume, score))

    print("\n📊 Ranking Results:")
    for name, score in sorted(results, key=lambda x: x[1], reverse=True):  # ✅ No need to convert to int again
        print(f"{name}: {score}")

if __name__ == "__main__":
    asyncio.run(process_resumes())  # ✅ Run async function
    print("\n✅ Process completed successfully!")