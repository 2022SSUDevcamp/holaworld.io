# holaworld.io

### Crawling.py
- 크롤링을 진행하며, DB.py의 클래스를 import하여
- MySQL에 크롤링한 데이터를 저장하는 함수를 호출하는 과정까지를 담고 있습니다.

### DB.py
- 크롤링된 데이터를 TblCrawlingData 객체에 담아
- Repo 객체에게 전달하여 저장하는 과정을 하고 있습니다. 
- 데이터를 MySQL 테이블에 저장하는 과정을 담고 있고, 구체적인 실행 코드는 없습니다.
  - 외부 python 파일에서 해당 파일의 클래스를 import하여 크롤링 및 Slack 알림 기능을 구현할 예정입니다.
