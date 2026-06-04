from openai import OpenAI
from src.config import OPENAI_API_KEY, BASE_MODEL


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def simplify_zero_shot(sentence):

    prompt = (
        "Simplify this sentence while preserving meaning:\n"
    )

    response = client.chat.completions.create(
        model=BASE_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt + sentence
            }
        ],
        temperature=0.3
    )


    return response.choices[0].message.content



def simplify_fine_tuned(
    sentence,
    model_id
):

    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {
            "role": "system",
            "content": "Rewrite the user's text in simpler English. Do not explain. Do not add new information. Output only the simplified sentence."
            },
            {
                "role": "user",
                "content": sentence
            }
        ]
    )


    return response.choices[0].message.content