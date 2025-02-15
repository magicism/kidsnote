from fastapi import FastAPI
from app.chatbot import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "키즈노트 챗봇 API"}

@app.post("/chat")
def chat(input_text: str):
    response = get_response(input_text)
    return {"response": response}
