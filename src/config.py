import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)


BASE_MODEL = "gpt-4o-mini"


EMBEDDING_MODEL = "text-embedding-3-small"


SYSTEM_PROMPT = """
You are a text simplification assistant.

Rewrite complex text into simpler language
while preserving the original meaning.
"""