import os
import asyncio
from dotenv import load_dotenv
from ai_evaluator import AgentActions

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in the .env file.")

print("✅ Environment variables loaded successfully.")


if __name__ == "__main__":
    actions = AgentActions()
    asyncio.run(actions.process_resumes())  # ✅ Run async function
    print("\n✅ Process completed successfully!")