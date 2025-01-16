from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
from config import Config
from csv_manager import CsvManager


class WebDataProcessor:

    def is_new_data(post_number, data_dict):
        if len(data_dict.keys()) == 0:
            return True
        
        return max(list(map(int, data_dict.keys()))) < int(post_number)


    def get_recent_contests(count):
        """
        가장 최근 공모를 count만큼 리턴함
        """

        # csv파일 열어서 dictionary로 파싱
        data_dict = CsvManager.csv_to_dict_by_key(Config.POST_NUMBER_KEY)

        post_numbers = list(map(int, data_dict.keys()))
        post_numbers.sort(reverse=True)

        arr = []

        for i in range(count):
            post_number = post_numbers[i]
            arr.append(data_dict[str(post_number)])

        return arr


    def process_contest_check():
        """
        새로 올라온 공모의 개수를 확인하고, 새로 올라온 공모를 저장함
        
        Args:
            soup : 서울 청년주택 공식 홈페이지 - 공모공지 게시판 웹 크롤링 데이터
            tbody : 게시글 테이블
            new_data_dict : 새로 올라온 공고글 데이터
        """
        SELENIUM_URL = os.getenv("SELENIUM_URL","http://selenium:4444/wd/hub")
        # csv파일 열어서 dictionary로 파싱
        data_dict = CsvManager.csv_to_dict_by_key(Config.POST_NUMBER_KEY)


        # ChromeDriver 설정
        options = Options()
        options.add_argument("--headless")  # 브라우저 창을 열지 않음 (옵션)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer");
        options.add_argument("--disable-dev-shm-usage")

        # WebDriver 생성
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        #driver = webdriver.Remote(command_executor=SELENIUM_URL, options=options)

        # URL로 이동
        driver.get(Config.ANNOUNCEMENT_LINK)

        # 페이지가 JavaScript를 로드할 시간을 기다림
        time.sleep(0.5)  # 필요에 따라 조정

        # 페이지 소스 가져오기
        html = driver.page_source

        # BeautifulSoup으로 파싱
        soup = BeautifulSoup(html, 'html.parser')

        # tbody 태그 선택
        tbody = soup.select_one('tbody')

        result = 0
        # 공지사항 추출
        if tbody:
            rows = tbody.select('tr')

            new_data_dict = {}

            for row in rows:
                cols = row.find_all('td')
                if cols:
                    post_number = cols[0].text.strip()

                    # 새로운 글 번호 이면 new_data_dict에 저장
                    # 새로운 글 번호는 이전에 db에 저장해둔 글 번호들중 max값 보다 큰 값이라고 상정
                    if WebDataProcessor.is_new_data(post_number, data_dict):
                        post_title = cols[2].text.strip()  # 제목 (3번째 열)
                        post_url = Config.ROOT_RUL + cols[2].select_one('a').get('href') # 글링크 (3번쨰 열의 href태그 값)
                        post_date = cols[3].text.strip()  # 게시 날짜 (4번째 열)
                        application_date = cols[4].text.strip() # 청약 신청일 (5번째 열)

                        data = {
                            Config.POST_NUMBER_KEY : post_number,
                            Config.POST_TITLE_KEY : post_title,
                            Config.POST_URL_KEY : post_url,
                            Config.POST_DATE_KEY : post_date,
                            Config.APPLICATION_DATE_KEY : application_date
                        }
                        

                        new_data_dict[post_number] = data

            # 새로운 값이 있으면 db에 추가
            if len(new_data_dict.keys()) > 0:
                for new_key in new_data_dict.keys():
                    data_dict[new_key] = new_data_dict[new_key]

                # csv 저장
                CsvManager.save_dict_to_csv(data_dict)

                result = len(new_data_dict.keys())
            
        else:
            print("tbody 태그를 찾을 수 없습니다.")


        # 브라우저 닫기
        driver.quit()

        return result


if __name__ == "__main__":
    # print(WebDataProcessor.process_contest_check())
    print(WebDataProcessor.get_recent_contests(3))