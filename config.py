import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER","gemini")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
OPENAI_MODEL = os.getenv("OPENAI_MODEL","gpt-4o-mini")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL","gemini-3.5-flash-lite")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL","http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL","mistral:latest")

SUPPORTED_PROVIDERS = ["openai","gemini","ollama"]

SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    """You are a helpful chatbot with conversation memory.

        Use the conversation history provided in the messages.
        Remember information the user shares during the conversation.
        When asked what you know about the user, summarize relevant
        facts from previous messages.

        Never claim that you know nothing if the information is
        present in the conversation history."""
)


def get_configuration_error() -> str|None:
    if LLM_PROVIDER not in SUPPORTED_PROVIDERS:
        return (
            f"LLM PROVIDER is {LLM_PROVIDER} not in supported list"
        )
    if LLM_PROVIDER == "openai" and not OPENAI_API_KEY:
        return "OPENAI_API_KEY is missing, add it to your .env"
    if LLM_PROVIDER == "gemini" and not GEMINI_API_KEY:
        return "GEMINI_API_KEY is missing, add it to your .env"

    return None