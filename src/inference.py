"""
Inference module for generating simplified text
using an LLM model.
"""

from openai import OpenAI
from config import SYSTEM_PROMPT


client = OpenAI()


def simplify_text(text, model):
    """
    Generate simplified text from complex input.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content