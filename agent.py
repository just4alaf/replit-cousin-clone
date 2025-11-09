import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def ask_agent(prompt: str) -> str:
    try:
        thread = client.beta.threads.create()
        client.beta.threads.messages.create(thread_id=thread.id, role="user", content=prompt)
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=os.getenv("ASSISTANT_ID")
        )
        while run.status not in ["completed", "failed"]:
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run.status == "failed":
            return "Agent failed."
        return client.beta.threads.messages.list(thread_id=thread.id).data[0].content[0].text.value
    except Exception as e:
        return f"Error: {str(e)}"
