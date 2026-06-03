import json


def filter_training_pairs(df, sample_size=100):
    """
    Select complex-simple sentence pairs
    from Newsela dataset.
    """

    filtered = df[
        (df["id_complex"]
            .str.split("-")
            .str[-3]
            .astype(int) == 0)
        &
        (df["id_simple"]
            .str.split("-")
            .str[-3]
            .astype(int) == 4)
    ]

    return filtered.sample(
        n=sample_size,
        random_state=42
    )


def create_jsonl(df, output_file):
    """
    Convert dataset into OpenAI fine-tuning format.
    """

    with open(output_file, "w") as f:

        for _, row in df.iterrows():

            example = {
                "messages": [
                    {
                        "role": "user",
                        "content": row["prompt"]
                    },
                    {
                        "role": "assistant",
                        "content": row["completion"]
                    }
                ]
            }

            f.write(json.dumps(example) + "\n")