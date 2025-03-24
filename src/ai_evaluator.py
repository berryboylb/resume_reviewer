import os
from agents import Runner
import re
from dotenv import load_dotenv
from agent_module.evaluator import agent
from tools import AgentTools
from resume_parser import ResumeParser
from constant import JOB_DESCRIPTION

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in the .env file.")

class AgentActions():
    async def rank_resume(self, resume_text, job_description):
        # get the agent tools
        tools = AgentTools()
        agent.tools.append(tools.evaluate_response)

        # Run the agent
        runner = Runner()
        result = await runner.run(agent, f"Evaluate this resume:\n\n{resume_text}\n\nAgainst this job description:\n\n{job_description}")

        print(result.final_output)
        
        match = re.search(r"Relevance Score:\s*(\d+)/10", result.final_output)
        if match:
            return int(match.group(1))  # Extract and return the integer score
        match = re.search(r"Response Evaluation Score:\s*(\d+)/10", result.final_output)
        if match:
            return int(match.group(1))  # Extract and return the integer score
        
        return 0
    
    async def process_resumes(self):
        resumes = [f for f in os.listdir("data/") if f.endswith((".pdf", ".docx"))]
        results = []

        for resume in resumes:
            print(f"🔍 Processing {resume}...")
            resume_parser = ResumeParser()
            text = resume_parser.extract_text(f"data/{resume}")
            score = await self.rank_resume(text, JOB_DESCRIPTION)  # ✅ Await async function
            results.append((resume, score))

        print("\n📊 Ranking Results:")
        for name, score in sorted(results, key=lambda x: x[1], reverse=True):  # ✅ No need to convert to int again
            print(f"{name}: {score}")

