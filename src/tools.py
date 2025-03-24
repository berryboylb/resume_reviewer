from agents import Runner, function_tool
from src.agent_module.performance import agent


class AgentTools():
    @function_tool
    async def evaluate_response(response: str) -> str:
        runner = Runner()
        result = await runner.run(agent, f"Evaluate this AI-generated response:\n\n{response}")
        
        print("✅ Agent Evaluation:", result.final_output)
        return result.final_output