import csv

# 파일 이름 설정
filename = "board_data.csv"

# 데이터 저장 함수
def save_to_csv(data, filename):
    # CSV의 헤더(열 제목)
    fieldnames = ["글번호", "글제목", "글링크", "게시일", "신청일"]
    
    # 파일 쓰기 모드로 열기
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # 헤더 작성
        writer.writeheader()
        
        # 데이터 작성
        writer.writerows(data)

# 데이터 가져오기 함수
def load_from_csv(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        # CSV 데이터를 리스트로 반환
        return list(reader)

# 저장할 데이터 예제
board_data = [
    {"글번호": 101, "글제목": "[민간임대] 상봉역 제이스타상봉 입주자 추가모집공고문", "글링크": "https://soco.seoul.go.kr/youth/bbs/BMSR00015/view.do?boardId=6147&menuNo=400008&pageIndex=1&searchCondition=&searchKeyword=", "게시일": "2024-12-17", "신청일": "2024-12-17"},
]

# CSV에 데이터 저장
save_to_csv(board_data, filename)

# CSV에서 데이터 읽기
loaded_data = load_from_csv(filename)

# 가져온 데이터 출력
print("CSV에서 가져온 데이터:")
for row in loaded_data:
    print(row)