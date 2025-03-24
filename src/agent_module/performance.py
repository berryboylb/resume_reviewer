from agents import Agent, WebSearchTool
from agents.tool import UserLocation

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