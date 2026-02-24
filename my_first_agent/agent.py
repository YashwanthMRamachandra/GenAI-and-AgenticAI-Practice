from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv

load_dotenv()

def get_current_time(city: str) -> dict:
  """Returns the current time in the specified city"""
  return {"status": "success", "city": city, "time": "10:30AM"}
  

root_agent = Agent(
    model = "gemini-2.5-flash",
    name = "time_agent",
    description = "Tells the current time in the specified city",
    instruction = "You are a helpful assistant that tells the current time in the cities. Use the 'get_current_time' tool for this purpose.",
    tools = [get_current_time]
)
