from google.adk.runners import Runner
from google.genai import types
from agents.weather_agent import create_weather_agent
from sessions.session_manager import get_or_create_session

async def call_agent_async(query: str):
   print(f"\n>>> User Query: {query}")
   # 1️⃣ Init session context
   ctx = await get_or_create_session()
   
   # 2️⃣ Create agent
   agent = create_weather_agent()
   
   # 3️⃣ Create runner
   runner = Runner(
       agent=agent,
       app_name=ctx["app_name"],
       session_service=ctx["session_service"],
   )
   
   # 4️⃣ Prepare user message
   content = types.Content(
       role="user",
       parts=[types.Part(text=query)],
   )
   final_response_text = "Agent did not produce a final response"

   # 5️⃣ Execute agent
   async for event in runner.run_async(
       user_id=ctx["user_id"],
       session_id=ctx["session_id"],
       new_message=content,
   ):
       if event.is_final_response():
           if event.content and event.content.parts:
               final_response_text = event.content.parts[0].text
           elif event.actions and event.actions.escalate:
               final_response_text = (
                   f"Agent escalated: {event.error_message or 'No specific message.'}"
               )
           break
   print(f"<<< Agent Response: {final_response_text}")
   
   return final_response_text