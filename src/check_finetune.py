from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

job_id = "ftjob-ULo29riapippSnh2Ldc26yBU"

job = client.fine_tuning.jobs.retrieve(job_id)

print("Status:", job.status)

if job.fine_tuned_model:
    print("Model:", job.fine_tuned_model)