from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

from config import Config

# ChromeDriver 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 열지 않음 (옵션)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# WebDriver 생성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL로 이동
driver.get(Config.ANNOUNCEMENT_LINK)

# 페이지가 JavaScript를 로드할 시간을 기다림
time.sleep(3)  # 필요에 따라 조정

# 페이지 소스 가져오기
html = driver.page_source

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html, 'html.parser')

# tbody 태그 선택
tbody = soup.select_one('tbody')

# 공지사항 추출
if tbody:
    rows = tbody.select('tr')
    for row in rows:
        cols = row.find_all('td')
        if cols:
            post_number = cols[0].text.strip()
            post_title = cols[2].text.strip()  # 제목 (3번째 열)
            post_url = Config.ROOT_RUL + cols[2].select_one('a').get('href')
            post_date = cols[3].text.strip()  # 게시 날짜 (4번째 열)
            application_date = cols[4].text.strip() # 청약 신청일 (5번째 열)
            print(f"제목: {post_title}, 날짜: {post_date}, 신청일: {application_date}, 글링크: {post_url}")
else:
    print("tbody 태그를 찾을 수 없습니다.")

# 브라우저 닫기
driver.quit()