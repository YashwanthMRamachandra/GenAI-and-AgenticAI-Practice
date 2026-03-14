from google.adk.agents import Agent
from tools.get_weather import get_weather

MODEL_GEMINI_2_5_FLASH = "gemini-2.5-flash"

def create_weather_agent():
   return Agent(
       model=MODEL_GEMINI_2_5_FLASH,
       name="weather_agent",
       description="Provides weather info for specified cities",
       instruction=(
           "You are a helpful weather assistant. "
           "When the user asks for the weather in a specific city, "
           "use the 'get_weather' tool to find the information. "
           "If the tool returns an error, inform the user politely. "
           "If the tool is successful, present the weather report clearly."
       ),
       tools=[get_weather],
   )