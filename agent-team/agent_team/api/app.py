from fastapi import FastAPI
from pydantic import BaseModel
import logging
from conversations.orchestrator import call_agent_async

# Optional: suppress noisy logs
logging.getLogger("google").setLevel(logging.WARNING)
logging.getLogger("google.adk").setLevel(logging.WARNING)
logging.getLogger("google.genai").setLevel(logging.WARNING)

app = FastAPI(
   title="Weather Agent API",
   version="1.0.0",
)

# -------- Request / Response Models --------
class QueryRequest(BaseModel):
   query: str
class QueryResponse(BaseModel):
   response: str

# -------- API Endpoint --------
@app.post("/query", response_model=QueryResponse)
async def query_agent(request: QueryRequest):
   """
   Send a user query to the ADK weather agent.
   """
   answer = await call_agent_async(request.query)
   return QueryResponse(response=answer)