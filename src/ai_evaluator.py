import os
from agents import Runner
import re
from dotenv import load_dotenv
from src.agent_module.evaluator import agent
from src.tools import AgentTools
from src.resume_parser import ResumeParser
from src.constant import JOB_DESCRIPTION
from openai.types.responses import ResponseTextDeltaEvent
import asyncio

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in the .env file.")

class AgentActions():
    
   async def fake_data_streamer(self):
        for i in range(10):
            yield b'some fake data\n\n'
            await asyncio.sleep(0.5)
   async def rank_resume(self, resume_text, job_description):
    tools = AgentTools()
    agent.tools.append(tools.evaluate_response)

    runner = Runner()
    result = runner.run_streamed(agent, f"Evaluate this resume:\n\n{resume_text}\n\nAgainst this job description:\n\n{job_description}")
    
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
            yield event.data.delta  # Yield each chunk immediately

    
    # async def process_resumes(self):
    #     resumes = [f for f in os.listdir("data/") if f.endswith((".pdf", ".docx"))]
    #     results = []

    #     for resume in resumes:
    #         print(f"🔍 Processing {resume}...")
    #         resume_parser = ResumeParser()
    #         text = resume_parser.extract_text(f"data/{resume}")
    #         score = await self.rank_resume(text, JOB_DESCRIPTION)  # ✅ Await async function
    #         results.append((resume, score))

    #     print("\n📊 Ranking Results:")
    #     for name, score in sorted(results, key=lambda x: x[1], reverse=True):  # ✅ No need to convert to int again
    #         print(f"{name}: {score}")

