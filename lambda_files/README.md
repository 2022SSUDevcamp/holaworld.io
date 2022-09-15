멘토님, <br>
아래는 지금까지 생성한 함수 구성입니다. <br>
긴 과정의 글이지만, 너그럽게 읽고 문제가 무엇인지 알려주시면 정말 감사하겠습니다. <br>

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
 - 반복문 돌면서 최종 만들어진 문자열을 리턴 -> lambda_handler의 message 변수가 받는다.

## DB.py

### TblCrawlingData 클래스
- 테이블 각 행의 데이터를 추가하거나 제거하기 위한 클래스( ORM 기반 )
- ( 이상하게, 생성자 없이도 인자 받아 그대로 저장되는 현상 )
  - https://ubiquitous-sapphire-4da.notion.site/SQLAlchemy_ORM-93d1c923070b4d7e8b0ce2024bc22790

### Repo 클래스
- 생성자에서 데이터베이스와 연결
  - ( aws_rds 데이터베이스 이름, 스키마, 테이블은 밑에서 설명하겠습니다. )
- 연결한 후 세션 객체 생성

#### add_crawling_data() 함수 : 
- 파라미터 : name, content, additional, startDate, link 
  - ( 모두 데이터베이스의 각 항목에 속함 )
- 파라미터들을 TblCrawlingData 생성자에 담아 한 행의 각 정보가 담긴 TblCrawlingData 객체 생성 후 session에 add
- 모두 더해지면 commit

#### get_crawling_data() 함수 : 
- 파라미터 : name
  - ( 데이터베이스의 column 중 하나에 해당 , study인지 project인지 구분 )
- 해당 분야를 가진 데이터 행 및 오늘로부터 최대 7일 이전의 것들만 가져오기
- 받아온 결과를 리턴( = TblCrawlingData 객체의 리스트 ) -> Slack.py에서 
  - studyToSlack() 함수에서 호출되어 data 변수에 저장된다.
 
## 데이터베이스
- aws_rds 데이터베이스 endpoint, 스키마, 테이블명 필요하면 Slack에 요청 올려주세요. DM으로 보내드리겠습니다.
```
# SQL문
#CREATE TABLE tbl_crawling_data (
#    id INTEGER AUTO_INCREMENT PRIMARY KEY,
#    name VARCHAR(255), // study , project
#    content VARCHAR(255), // 제목 텍스트
#    link VARCHAR(1024), // 링크( Slack.py 에서 조합해서 링크를 문자열에 생성합니다. )
#    additional VARCHAR(1024), ( 사용하는 언어의 조합 - Slack.py에서 &문자를 기반으로 split하여 리스트로 변환 )
#    startDate DATETIME( 마감 날짜 )
#);
```
--------------------------------------------------------------------------------------------\
여기까지가 제가 만든 코드입니다.

AWS Lambda에서 함수를 만들고 실행한 결과
1. Crawl 과정에서 처음 한두번은 크롤링이 정상적으로 작동하나
  - 여러 번 반복하면 오래 걸리면서 연결 timeout이 발생합니다.
2. Slack 알림 과정에서 
  - 오프라인으로 aws_rds 열람하여 콘솔 출력 가능합니다.
  - aws_lambda에서 단순한 문자열 slack으로 전송 가능합니다.
  - 그러나 rds로부터 데이터를 가져와서 slack으로 전송 시 
    - 연결 과정에 timeout 발생하고, 실패합니다.
 
 저는 크롤링을 위한 lambda 함수를 따로 만들고, <br>
 slack 알림을 위한 lambda 함수를 따로 만들었습니다. <br>
 하지만 두 함수에서 같은 rds를 접근하여, 데이터를 저장하고 추출하는 일을 수행하게끔 <br>
 하려고 코드를 작성하였습니다. 그러나 작동하지 않습니다. <br>
 멘토님 환경에서는 가능할까요,,??? 그리고 문제가 무엇인지 알 수 있을까요???
