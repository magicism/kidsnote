import openai
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드 (로컬 실행 시 필요)
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# 디버깅: 환경 변수 확인
print(f"디버깅: OPENAI_API_KEY = {api_key}")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")

# OpenAI 클라이언트 설정
client = openai.OpenAI(api_key=api_key)

def get_response(input_text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": input_text}]
    )
    return response.choices[0].message.content
