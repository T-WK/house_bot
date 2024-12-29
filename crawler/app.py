from flask import Flask, jsonify, request
from web_data_processor import WebDataProcessor


import json


app = Flask(__name__)  # Flask 앱 인스턴스 생성

@app.route('/api/posts/check-new', methods=['GET'])
def check_new_post():
    """
    새로운 모집공고가 있는지 확인함
    """
    result = None
    try:
        # 공고 확인 결과: boolean
        is_new_post_exist =  WebDataProcessor.process_contest_check()
        
        result = {"status": "success", "data": is_new_post_exist}

    except Exception as e:
        result = {"status": "error", "message": str(e)}

    
    return jsonify(result)
    

@app.route('/api/posts/recent-post', methods=['GET'])
def get_recent_post():
    """
    저장된 가장 최근 게시글을 가져와 json string으로 반환
    """

    result = None
    try:
        data_dict = WebDataProcessor.get_latest_contests()
    
        # 딕셔너리를 JSON 문자열로 변환
        json_string = json.dumps(data_dict, ensure_ascii=False)

        result = {"status": "success", "data": json_string}

    except Exception as e:
        result =  {"status": "error", "message": str(e)}

    
    return jsonify(result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # 서버 실행