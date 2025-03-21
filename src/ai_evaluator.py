import os
import asyncio
from agents import Agent, Runner, WebSearchTool, FileSearchTool, function_tool
from agents.tool import UserLocation
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key! Set it in the .env file.")

@function_tool
async def evaluate_response(response: str) -> str:
    instructions = """
    You are a performance manager. Your duty is to evaluate responses from AI agents
    and provide feedback. Playfully rank resumes by using short words and emojis. on what you think about their response.
    """

    agent = Agent(
        name="Performance Manager",
        instructions=instructions,
        model="gpt-4o-mini",
        tools=[
            WebSearchTool(
                user_location=UserLocation(
                    type="approximate",
                    city="San Francisco",
                    country="US",
                )
            ),
        ],
    )

    runner = Runner()
    result = await runner.run(agent, f"Evaluate this AI-generated response:\n\n{response}")
    
    print("✅ Agent Evaluation:", result.final_output)

    return result.final_output


async def rank_resume(resume_text, job_description):
    instructions = """You are a experienced resume evaluator. Compare resumes with jobs matching the job descriptions in their city and provide a relevance score (0-10).
    When checking resumes, use the following criteria:
    - Use the web_search tool to search for the latest relevant job postings before evaluation.
    - show the job posting and make sure it is relevant to the  job description.
    - Break down and give comprehensive feedback on the resume on key areas to improve, keys words to focus on, areas to avoid and the current resume ATS score.
    - use the evaluate_response to get feedback on the response you gave the user always add a relevance score in your response.
    - Make sure the relevance score is not lost in the process and always returned
    - The evaluate_response feedback should come after the evaluation has been completed
    """

    # Define the agent
    agent = Agent(
        name="ResumeRanker",
        instructions=instructions,
        model="gpt-4o-mini",
        tools=[
            WebSearchTool(
                user_location=UserLocation(
                    type="approximate",
                    city="San Francisco",
                    country="US",
                )
            ),
            # FileSearchTool(vector_store_ids=["default"]),
        ],
    )
    agent.tools.append(evaluate_response)

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

