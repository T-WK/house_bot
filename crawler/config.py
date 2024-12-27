class Config:
    ROOT_RUL = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/"
    ANNOUNCEMENT_LINK = "https://soco.seoul.go.kr/youth/bbs/BMSR00015/list.do?menuNo=400008"
    
    #csv 파일명
    CSV_FILENAME = "./crawler/board_data.csv"

    # dict key
    POST_NUMBER_KEY = "post_number"
    POST_TITLE_KEY = "post_title"
    POST_URL_KEY = "post_url"
    POST_DATE_KEY = "post_date"
    APPLICATION_DATE_KEY = "application_date"

    # logo
    LOGO_FILE_PATH = "../logo/crawler_logo.txt"
