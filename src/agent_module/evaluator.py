from agents import Agent, WebSearchTool
from agents.tool import UserLocation

instructions = """You are a experienced resume evaluator. Compare resumes with jobs matching the job descriptions in their city and provide a relevance score (0-10).
    When checking resumes, use the following criteria:
    - Use the web_search tool to search for the latest relevant job postings before evaluation.
    - show the job posting, attach the link you got it from and make sure it is relevant to the  job description.
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