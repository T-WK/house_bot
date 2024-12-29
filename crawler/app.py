from flask import Flask, jsonify, request
from web_data_processor import WebDataProcessor


import json


app = Flask(__name__)  # Flask 앱 인스턴스 생성

@app.route('/api/posts/new-counts', methods=['GET'])
def check_new_post_count():
    """
    새로운 모집공고가 있는지 확인함
    """
    result = None
    try:
        # 공고 확인 결과: int => 새로운 공고 개수
        is_new_post_exist =  WebDataProcessor.process_contest_check()
        
        result = {"status": "success", "data": is_new_post_exist}

    except Exception as e:
        result = {"status": "error", "message": str(e)}

    
    return jsonify(result)
    

@app.route('/api/posts/recent-posts', methods=['GET'])
def get_recent_post():
    """
    저장된 가장 최근 게시글을 가져와 json string으로 반환
    """

    result = None
    try:
        count = int(request.args.get('count', default=1))
        data_arr = WebDataProcessor.get_recent_contests(count)

        # 배열 그대로를 리턴
        result = {"status": "success", "data": data_arr}

    except Exception as e:
        result =  {"status": "error", "message": str(e)}

    
    return jsonify(result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # 서버 실행