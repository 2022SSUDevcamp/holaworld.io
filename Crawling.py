import requests
import json
from temp_DB import Repo
from temp_DB import TblCrawlingData
from sqlalchemy import create_engine, text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry, Session 
from datetime import datetime

if __name__ == "__main__":
    # limit만 내가 수정해서 크롤링 하면 된다.
    url = "https://api.holaworld.io/api/posts?sort=-createdAt&offset=0&limit=1000&isClosed=false&type=0"
    response = requests.get(url)

    data = json.loads(response.text)

    for datum in data:
        
        # language = 언어 리스트
        # isClosed = boolean 값
        # startDate = '2022-09-04T15:16:00.000Z'
        # endDate : 없는 듯
        # comments = 댓글 딕셔너리 리스트
        # id = 스터디에 지정된 id primary key 값

        #print(datum.get('isClosed')) # 마감 여부
        #print(datum.get("language")) # 사용 언어
        #print(datum.get("title")) # 타이틀
        #print(datum.get("hashTags")) # 해시태그 - 대부분 없다고 나옴
        #print(datum.get("startDate")) # 시작 날짜
        #print("----")

        # print(datum.keys()) # 각 항목의 key를 얻을 수 있다.

        # additional : 사용할 언어 / 프레임워크
        langs = datum.get("language")
        additional = '&'.join(langs)
        # print( datum.get('type')) # 

        # id
        iden = datum.get("id") 
        #print(iden)

        # name , 1이면 프로젝트 , 2이면 스터디 , 모집 완료되면 0
        isClosed = datum.get('isCLosed')
        name = datum.get("name")
        if name == '1':
            name = 'Project'
        elif name == '2':
            name = 'Study'
        if isClosed == True:
            name = 'Closed'
        
        # content : 텍스트
        content = datum.get("title")

        # startDate : 시작 날짜 / # 2021-11-23T02:50:35.772Z
        startDate = datum.get("startDate")
        startDate = startDate[:10]
        #Time = startDate[11:19]
        #startDate = Date + " " + Time
        startDate = datetime.strptime(startDate, '%Y-%m-%d')
        #print(startDate, type(startDate))

        repo = Repo()
        repo.add_crawling_data(name, content, additional, startDate)

        # id : 프로젝트 Serial No
        # name : 모집 종류 / 프로젝트(1) / 스터디(2) / 모집됨(0)
        # content : 텍스트
        # additional : 언어 리스트
        # startDate : 시작 예정일


