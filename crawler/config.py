class Config:
    ROOT_RUL = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/"
    ANNOUNCEMENT_LINK = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008"
    
    #csv 파일명
    CSV_FILENAME = "./crawler/board_data.csv"

    # dict key
    POST_NUMBER_KEY = "글번호"
    POST_TITLE_KEY = "제목"
    POST_URL_KEY = "글링크"
    POST_DATE_KEY = "게시일"
    APPLICATION_DATE_KEY = "신청일"
