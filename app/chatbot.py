import openai
import os

# OpenAI API 키 설정
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(input_text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": input_text}]
    )
    return response.choices[0].message.content  # 최신 API 형식 적용
