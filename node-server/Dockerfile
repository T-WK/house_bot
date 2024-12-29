# Node.js 이미지 사용
FROM node:16

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 설치
COPY package.json package-lock.json ./
RUN npm install

# 서버 파일 복사
COPY . .

# 앱 실행
CMD ["node", "index.js"]