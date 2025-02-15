import openai
import os

# API Key 설정 (환경변수 사용 권장)
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": input_text}]
    )
    return response["choices"][0]["message"]["content"]
