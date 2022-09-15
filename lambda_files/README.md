# lambda_function.py

### lambda_handler(event, context)
- aws lambda 환경 상에서 main 함수의 역할
- slack의 bot을 사용하였더니 작동하지 않아서 저 혼자만 속해 있는 slack 채널에 webhook 앱(봇)을 새로 만들어 slack 메세지를 보내려고 했습니다.

### post_slack(argStr) 함수 : 
- 받은 문자열(argStr)을 사용하여 slack으로 문자 보내는 함수
- argStr은 slack 보내기 위한 'Slack' 클래스에서 전체 내용 담긴 문자열을 받는다.
- 문자열 받는 함수 : Slack.studyToSlack() -> 스터디 항목 받기 위한 함수
-                   Slack.projectToSlack() -> 프로젝트 항목 받기 위한 함수



## class Slack ( from Slack.py )

### studyToSlack(self): ( 그 아래에 projectToSlack(self) 함수 역시 구조는 동일하다. )
- 데이터베이스를 다루기 위한 DB.py의 Repo 클래스 객체 선언한다.
- repo에서 데이터를 가져오는 get_crawling_data() 함수 호출
  - 파라미터 : 프로젝트인지 , 스터디인지 구분하는 키워드( 'Study' 혹은 'Project' )
  - 받아온 데이터 리스트( data 리스트 변수 ) = DB.py의 TblCrawlingData 클래스들로 이루어져 있음
  - for 문 돌면서 각 column의 항목 받아 문자열로 변환 후 message에 추가로 붙여 넣기
