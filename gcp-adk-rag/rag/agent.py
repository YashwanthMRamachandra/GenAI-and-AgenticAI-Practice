import os
import uuid

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import (
    VertexAiRagRetrieval,
)
from openinference.instrumentation import using_session
from vertexai.preview import rag

# from rag.tracing import instrument_adk_with_azire

#from .prompts import return_instructions_root