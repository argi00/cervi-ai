print('Hello, Lightning World!')
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Question(BaseModel):
    question: str

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/ask")
def ask_ai(data: Question):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "cervi-ai",
            "prompt": data.question,
            "stream": False
        }
    )

    return {"answer": response.json()["response"]}