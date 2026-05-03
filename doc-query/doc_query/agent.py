import asyncio

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.adk.tools import VertexAiSearchTool

# Data Stores
from settings import DATASTORE_PATH

from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Constants
APP_NAME_VSEARCH = "vertex_search_app"
USER_ID_VSEARCH = "user_vsearch_1"
SESSION_ID_VSEARCH = "session_vsearch_1"
AGENT_NAME_VSEARCH = "doc_query"
GEMINI_2_FLASH = "gemini-2.5-flash"

# Tool instantiation
vertex_ai_search_tool = VertexAiSearchTool(
    data_store_id=DATASTORE_PATH
)

# Agent Definition
doc_query = LlmAgent(
    name=AGENT_NAME_VSEARCH,
    model=GEMINI_2_FLASH,
    tools=[vertex_ai_search_tool],
    instruction=f"""
    You are a helpful assistant that answers questions based on information found in the document store: {DATASTORE_PATH}.
    Use the search tool to find relevant information before answering.
    If the answer isn't in the documents, say that you couldn't find the information.
    """,
    description="Answers questions using a specific Agent Search datastore.",
)

# Session and Runner setup
session_service_vsearch = InMemorySessionService()
runner_vsearch = Runner(
    agent=doc_query,
    session_service=session_service_vsearch,
    app_name=APP_NAME_VSEARCH,
)

root_agent = doc_query

# session_vsearch = session_service_vsearch.create_session(
#     session_id=SESSION_ID_VSEARCH,
#     user_id=USER_ID_VSEARCH,
#     app_name=APP_NAME_VSEARCH,
# )

# Agent interaction function
async def call_vsearch_agent_async(query: str):
    print(f"\n--- Running Search Agent ---")
    print(f"Query: {query}")

    content = types.Content(role="user", parts=[types.Part(text=query)])
    final_response_text = "No response received"

    try:
        async for event in runner_vsearch.run_async(
            user_id=USER_ID_VSEARCH, session_id=SESSION_ID_VSEARCH, new_message=content
        ):
            # Like Google Search, results are often embedded in the model's response.
            if event.is_final_response() and event.content and event.content.parts:
                final_response_text = event.content.parts[0].text.strip()
                print(f"Agent Response: {final_response_text}")
                # You can inspect event.grounding_metadata for source citations
                if event.grounding_metadata:
                    print(
                        f"  (Grounding metadata found with {len(event.grounding_metadata.grounding_attributions)} attributions)"
                    )

    except Exception as e:
        print(f"An error occurred: {e}")
        print(
            "Ensure your datastore ID is correct and the service account has permissions."
        )
    print("-" * 30)

# --- Run Example ---
async def runner_vsearch_example():
    # Replace with a question relevant to YOUR datastore content
    await call_vsearch_agent_async(
        "Identify all the L2 Domains present in both Structured and Unstructured Data"
    )
    await call_vsearch_agent_async(
        "List down all the Business Objective(BO) present in both Structured and Unstructured Data"
    )

# Execute the example
# await run_vsearch_example()

# Running locally due to potential colab asyncio issues with multiple awaits
# if __name__ == "__main__":
#     try:
#         asyncio.run(runner_vsearch_example())
#     except Exception as e:
#         if "cannot be called from a running event loop" in str(e):
#             print("Skipping execution in running event loop (like Colab/Jupyter). Run locally.")
#         else:
#             raise e

if __name__ == "__main__":
    print(f"Run using: adk web")
