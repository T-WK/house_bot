# Python 이미지를 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필수 라이브러리 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# 앱 파일 복사
COPY . .

# 포트 열기
EXPOSE 8080

# Flask 앱 실행
CMD ["python3", "app.py"]
