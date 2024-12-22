import csv
from config import Config

# 파일 이름 설정



class CsvManager:

    # CSV 데이터를 글번호를 기준으로 딕셔너리로 저장하는 함수
    def csv_to_dict_by_key(key):
        result = {}
        with open(Config.CSV_FILENAME, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                result[row[key]] = dict(row)  # key를 기준으로 딕셔너리에 저장
        return result

    # CSV 데이터를 딕셔너리에 저장하는 함수
    def save_dict_to_csv(data):
        if not data:
            raise ValueError("저장할 데이터가 없습니다.")
        
        # CSV의 헤더(열 이름) 가져오기 (첫 데이터 기준)
        fieldnames = list(next(iter(data.values())).keys())
        
        with open(Config.CSV_FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # 헤더 작성
            writer.writeheader()
            
            # 데이터 작성
            for row in data.values():
                writer.writerow(row)




if __name__ == "__main__":
    # 저장할 데이터 예제
    board_data_by_key = {
        "1": {"글번호": "1", "글제목": "첫 번째 공지사항", "글링크": "https://example.com/1", "게시일": "2024-12-20", "신청일": "2024-12-25"},
        "2": {"글번호": "2", "글제목": "두 번째 공지사항", "글링크": "https://example.com/2", "게시일": "2024-12-21", "신청일": "2024-12-26"},
    }

    # CSV에 데이터 저장
    CsvManager.save_dict_to_csv(board_data_by_key)

    # CSV에서 데이터 읽기
    loaded_data = CsvManager.csv_to_dict_by_key("글제목")

    # 가져온 데이터 출력
    print("CSV에서 가져온 데이터:")
    for row in loaded_data:
        print(row)