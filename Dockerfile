# 베이스 이미지 (Python 최신 버전 사용)
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY . /app

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너 실행 명령
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
ENV OPENAI_API_KEY="your_openai_api_key
