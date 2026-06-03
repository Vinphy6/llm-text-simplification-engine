"""
Prepare text data for OpenAI fine-tuning.

OpenAI fine-tuning requires training data
formatted as conversational examples.
"""

import json


def create_training_example(complex_text, simplified_text):
    """
    Convert an input/output pair into OpenAI chat format.
    """

    return {
        "messages": [
            {
                "role": "system",
                "content": (
                    "Simplify complex text while preserving meaning."
                ),
            },
            {
                "role": "user",
                "content": complex_text,
            },
            {
                "role": "assistant",
                "content": simplified_text,
            },
        ]
    }


def save_training_file(examples, output_path):
    """
    Save examples as JSONL file for fine-tuning.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        for example in examples:
            file.write(json.dumps(example) + "\n")