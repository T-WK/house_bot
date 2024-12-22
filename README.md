# -_-
쳥년주택 모집공고 확인 봇


기능 리스트

- API 소개
    - /api
        - /posts/check-new : 새로운 공모글이 있는지 확인함
            - result
                - 처리에 성공 했을 경우
                    - "status"
                        -  "success"
                    - "data"
                        - True : 새로운 공모가 올라옴
                        - False : 새로운 공모가 없음

                - 처리에 실패 했을 경우
                    - "status"
                        - "error"  
                    - "message" : 실패사유 메시지 (exeption 메시지)


            - api 호출 예시
                ```
                서버 주소(아직 없음)/api/posts/check-new
                ```
            - api 호출성공 시 결과값 예시
                ```
                {
                    "data": true,
                    "status": "success"
                }
                ```

        - /posts/recent-post : 가장 최근 공모를 가져옴
            - result
                - 처리에 성공했을 경우
                    - "status"
                        -  "success"
                    - "data" : 아래 정보를 가지고 있는 json string
                        - "글번호" : 공모 게시글 번호
                        - "글제목" : 공모 게시글 제목
                        - "글링크" : 공모 게시글의 링크
                        - "게시일" : 공모 게시글 등록일
                        - "신청일" : 청약신청 시작일

            - api 호출 예시
                ```
                서버 주소(아직 없음)/posts/recent-post
                ```
            - api 호출성공 시 결과값 예시
                ```
                {
                    "data": "{\"글번호\": \"1\", \"제목\": \"[민간] 새로운 공고글\", \"글링크\": \"https://example.html", \"게시일\": \"20xx-xx-xx\", \"신청일\": \"20xx-xx-xx\"}",
                    "status": "success"
                }
                ```

                

- 년도별 공모확인. -> 날짜별 공모 확인도 가능하면 재밌을듯. (진행예정)

- 코드 동작 로그 파일 작성.