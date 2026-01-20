import os
import asyncio
import warnings
import logging

from google.colab import userdata
from conversations.orchestrator import call_agent_async

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.WARNING)

logging.getLogger("google").setLevel(logging.WARNING)
logging.getLogger("google.adk").setLevel(logging.WARNING)
logging.getLogger("google.genai").setLevel(logging.WARNING)

# Environment setup
# os.environ["GEMINI_API_KEY"] = userdata.get("GOOGLE_API_KEY")
# print(os.environ["GEMINI_API_KEY"])

async def run_conversation():
   await call_agent_async("What is the weather like in London?")
   await call_agent_async("How about Paris?")
   await call_agent_async("Tell me the weather in New York")

if __name__ == "__main__":
   asyncio.run(run_conversation())