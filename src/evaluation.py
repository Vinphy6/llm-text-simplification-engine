import textstat
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

from src.config import (
    OPENAI_API_KEY,
    EMBEDDING_MODEL
)


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def readability_score(text):

    return {
        "reading_ease":
            textstat.flesch_reading_ease(text),

        "grade_level":
            textstat.flesch_kincaid_grade(text)
    }



def get_embedding(text):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding



def semantic_similarity(
        original,
        simplified
):

    emb1 = get_embedding(original)
    emb2 = get_embedding(simplified)

    return cosine_similarity(
        np.array(emb1).reshape(1,-1),
        np.array(emb2).reshape(1,-1)
    )[0][0]