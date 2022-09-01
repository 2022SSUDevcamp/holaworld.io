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

- SQL문
```
# -- auto-generated definition
# CREATE TABLE tbl_crawling_data
# (
#   id      int AUTO_INCREMENT PRIMARY KEY, # 자동으로 생성되는 id 
        # ( 원래 태그 내에 id가 있었으나 Base 클래스에 id 있어서 충돌 발생 )
#   name    varchar(255)  NULL, # 분야 구분 ( 마감 : 0 / 프로젝트 : 1 / 스터디 : 2 ) 
#   content varchar(1024) NULL, # 제목 ( title , 텍스트 )
#   additionals varchar(1024) NULL, # ( 사용하는 언어 저장 , 하나의 문자열로 저장 - 구분자를 &으로 설정 )
#   startDate datetime NULL # ( 시작 날짜 )
# );
```
