import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_jsonl(input_json, output_jsonl):
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(output_jsonl, "w", encoding="utf-8") as f:
        for item in data:
            record = {
                "messages": [
                    {
                        "role": "system",
                        "content": "Simplify complex English text while preserving the original meaning."
                    },
                    {
                        "role": "user",
                        "content": item["complex"]
                    },
                    {
                        "role": "assistant",
                        "content": item["simple"]
                    }
                ]
            }
            f.write(json.dumps(record) + "\n")


def upload_training_file(jsonl_path):
    file = client.files.create(
        file=open(jsonl_path, "rb"),
        purpose="fine-tune"
    )
    return file.id


def start_fine_tuning(training_file_id, model="gpt-4o-mini-2024-07-18"):
    job = client.fine_tuning.jobs.create(
        training_file=training_file_id,
        model=model
    )
    return job.id


def check_fine_tuning_job(job_id):
    job = client.fine_tuning.jobs.retrieve(job_id)
    return job


if __name__ == "__main__":
    create_jsonl(
        "data/training_data.json",
        "data/training_data.jsonl"
    )

    file_id = upload_training_file("data/training_data.jsonl")
    print("Uploaded file:", file_id)

    job_id = start_fine_tuning(file_id)
    print("Fine-tuning job started:", job_id)