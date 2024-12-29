# -_-
쳥년주택 모집공고 확인 봇


기능 리스트

- API 소개
    - /api
        - /posts/new-counts : 새로운 공모글의 개수를 가져옴
            - result
                - 처리에 성공 했을 경우
                    - "status"
                        -  "success"
                    - "data"
                        - 새로운 공고의 개수 (정수)

                - 처리에 실패 했을 경우
                    - "status"
                        - "error"  
                    - "message" : 실패사유 메시지 (exeption 메시지)


            - api 호출 예시
                ```
                서버 주소(아직 없음)/api/posts/new-counts
                ```
            - api 호출성공 시 결과값 예시
                ```
                {
                    "data": 3,
                    "status": "success"
                }
                ```

        - /posts/recent-posts?count={개수} : 가장 최근 공모를 count만큼 가져옴 (기본값=1)
            - result
                - 처리에 성공했을 경우
                    - "status"
                        -  "success"
                    - "data" : 아래 정보를 가지고 있는 json array
                    ```
                        [
                            {
                                "post_number" : 공모 게시글 번호
                                "post_title" : 공모 게시글 제목
                                "post_url" : 공모 게시글의 링크
                                "post_date" : 공모 게시글 등록일
                                "application_date" : 청약신청 시작일
                            },
                            ...
                        ]
                    ```

            - api 호출 예시
                ```
                서버 주소(아직 없음)/api/posts/recent-posts?count=1
                ```
            - api 호출성공 시 결과값 예시
                ```
                {   
                    "data": [
                        {
                            "post_number" : 공모 게시글 번호
                            "post_title" : 공모 게시글 제목
                            "post_url" : 공모 게시글의 링크
                            "post_date" : 공모 게시글 등록일
                            "application_date" : 청약신청 시작일
                        },
                    ],
                    "status": "success"
                }
                ```

                

- 년도별 공모확인. -> 날짜별 공모 확인도 가능하면 재밌을듯. (진행예정)

- 코드 동작 로그 파일 작성.