# holaworld.io

### Crawling.py
- 크롤링을 진행하며, DB.py의 클래스를 import하여
- MySQL에 크롤링한 데이터를 저장하는 함수를 호출하는 과정까지를 담고 있습니다.

### DB.py
- 크롤링된 데이터를 TblCrawlingData 객체에 담아
- Repo 객체에게 전달하여 저장하는 과정을 하고 있습니다. 
- 데이터를 MySQL 테이블에 저장하는 과정을 담고 있고, 구체적인 실행 코드는 없습니다.
  - 외부 python 파일에서 해당 파일의 클래스를 import하여 크롤링 및 Slack 알림 기능을 구현할 예정입니다.

### SQL 스키마 - 테이블
- 스키마 : `project_` 로 이름 설정
- 테이블 : `tbl_crawling_data`로 설정

- SQL문( 초기 스키마 및 테이블 설정 - workbench )
```
# SQL문
#CREATE TABLE tbl_crawling_data (
#    id INTEGER AUTO_INCREMENT PRIMARY KEY, # ID - INTEGER 값 - 임의로 점차 증가
#    name VARCHAR(255), # 분야 ( Study / Project / 마감됨 )
#    content VARCHAR(255), # 제목
#    link VARCHAR(1024), # 링크 - json의 #id값 - `https://holaworld.io/study혹은project/id명` 의 형식
#    additional VARCHAR(1024), # 사용할 언어 혹은 프레임워크
#    startDate DATETIME # 시작 날짜
#);
```

### Slack.py
- 데이터베이스에 저장된 항목들을 가져온다.
  - 기준: name이 Study 혹은 Project인 것( 각각 따로 Database에서 추출 ) && startDate가 오늘 기준으로 일주일 안에 있는 것
  - 위의 SQL문의 link 테이블의 주석대로 링크를 생성해서 따라가 보니 404 Error 발생하는 경우 있음
    - 직접 들어가 보니 프로젝트인데도 study로 구분된 경우가 있음 - 에러 처리를 해야 함 
  - 프로젝트 구분은 프로젝트로 , 스터디 구분은 스터디로 따로 나눠서 각각 SlackBot으로 전송하여 Slack 채널에 
