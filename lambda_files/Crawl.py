import requests
import json
from DB import Repo
from DB import TblCrawlingData
from datetime import datetime

class Crawl:

    def holaworld_Crawl(self):
        # limit만 내가 수정해서 크롤링 하면 된다.
        url = "https://api.holaworld.io/api/posts?sort=-createdAt&offset=0&limit=1000&isClosed=false&type=0"
        response = requests.get(url)

        data = json.loads(response.text)
        repo = Repo()

        for datum in data:
            
            # language = 언어 리스트
            # isClosed = boolean 값
            # startDate = '2022-09-04T15:16:00.000Z'
            # endDate : 없는 듯
            # comments = 댓글 딕셔너리 리스트
            # id = 스터디에 지정된 id primary key 값

            # print(datum.keys()) # 각 항목의 key를 얻을 수 있다.

            # additional : 사용할 언어 / 프레임워크
            langs = datum.get("language")
            additional = '&'.join(langs)
            # print( datum.get('type')) # 

            # id
            iden = datum.get("id") 
            #print(iden)

            # name , 1이면 프로젝트 , 2이면 스터디 , 모집 완료되면 0
            isClosed = datum.get('isClosed')
            name = datum.get("type") # 2 , 1이지만 , 문자열
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
            startDate = startDate[:10] # 날짜
            #Time = startDate[11:19] # 시간 
            #startDate = Date + " " + Time # 시간 + 날짜
            startDate = datetime.strptime(startDate, '%Y-%m-%d') # 날짜만 생성하기로 하였습니다.

            # 링크 = holaworld.io/study혹은project/id명 - name 변수를 lower() 처리하여 조합해야 함
            link = datum.get('id')# 일단 id만 저장하고 , 나중에 불러올 때 링크를 조합할 예정

            repo.add_crawling_data(name, content, additional, startDate, link)

    def funsys_crawl(self):

        repo = Repo()

        for i in range(1, 4):
            # 1 to 3 - 보통 3페이지까지가 모집 중 데이터에 해당
            url = f'https://fun.ssu.ac.kr/ko/program/all/list/all/{i}'

            
            # 얘는 json 타입이 아니여서 그냥 BeautifulSoup으로 크롤링해야 함
            response = requests.get(url)
            html = response.text

            soup = BeautifulSoup(html, "html.parser")

            # SQL문
            #CREATE TABLE tbl_crawling_data (
            #    id INTEGER AUTO_INCREMENT PRIMARY KEY,
            #    name VARCHAR(255),
            #    content VARCHAR(255),
            #    link VARCHAR(1024),
            #    additional VARCHAR(1024),
            #    startDate DATETIME
            #);

        # ------------------------------------------- OPEN ------------------------------------------------------------------
            list = soup.select(".OPEN")
            #print("----------------------------OPEN------------------------------")
            for item in list:
                parent = item.parent # 부모 태그  
                # print(type(parent))

                # 제목
                content = parent.find("div", {"class": "detail"}).find("div", {"data-role": "default"}).find("div", {"class": "content"})
                title = content.find("b", {"class": "title"})
                title = title.text
                #print("제목 : ", title.text)

                # 링크
                link = 'https://fun.ssu.ac.kr'+parent['href'] 
                #print("링크 : ", link)

                # 구분
                name = 'open'
                #print("구분 : ", name)

                # 마감 일자 = duedate
                startDate = parent.find("div", {"class": 'content'}).find_all("small")[2].find_all("time")[1]
                startDate = startDate['datetime'][:10]
                startDate = datetime.strptime(startDate, '%Y-%m-%d')
                #print("마감 일자 : ", startDate['datetime'])

                # 주최
                additional = content.find('label').text # 주최 
                #print("주최 : ", additional)

                #print("----------------------------------------------------------")

                repo.add_crawling_data(name, title, additional, startDate, link)
            
        # ------------------------------------------- APPROACHING ------------------------------------------------------------------
            list = soup.select(".APPROACHING")
            # print("--------------------------APPROACHING--------------------------------")
            for item in list:
                parent = item.parent # 부모 태그  
                # print(type(parent))

                # 제목
                content = parent.find("div", {"class": "detail"}).find("div", {"data-role": "default"}).find("div", {"class": "content"})
                title = content.find("b", {"class": "title"})
                title = title.text
                # print("제목 : ", title.text)

                # 링크
                link = 'https://fun.ssu.ac.kr'+parent['href'] 
                # print("링크 : ", link)

                # 구분
                name = 'approaching'
                # print("구분 : ", name)

                # 마감 일자
                startDate = parent.find("div", {"class": 'content'}).find_all("small")[2].find_all("time")[1]
                startDate = startDate['datetime'][:10]
                startDate = datetime.strptime(startDate, '%Y-%m-%d')

                # print("마감 일자 : ", startDate['datetime']) 

                # 주최
                additional = content.find('label').text # 주최 
                # print("주최 : ", additional)

                # print("----------------------------------------------------------")

                repo.add_crawling_data(name, title, additional, startDate, link)
            
        # ------------------------------------------- APPROACH_CLOSING ------------------------------------------------------------------
            list = soup.select(".APPROACH_CLOSING")
            # print("---------------------------APPROACH_CLOSING-------------------------------")
            for item in list:
                parent = item.parent # 부모 태그  
                # print(type(parent))

                # 제목
                content = parent.find("div", {"class": "detail"}).find("div", {"data-role": "default"}).find("div", {"class": "content"})
                title = content.find("b", {"class": "title"})
                title = title.text
                # print("제목 : ", title.text)

                # 링크
                link = 'https://fun.ssu.ac.kr'+parent['href'] 
                # print("링크 : ", link)

                # 구분
                name = 'approach_closing'
                # print("구분 : ", name)

                # 마감 일자
                startDate = parent.find("div", {"class": 'content'}).find_all("small")[2].find_all("time")[1]
                startDate = startDate['datetime'][:10]
                startDate = datetime.strptime(startDate, '%Y-%m-%d')
                # print("마감 일자 : ", startDate['datetime'])

                # 주최
                additional = content.find('label').text # 주최 
                # print("주최 : ", additional)

                # print("----------------------------------------------------------")

                repo.add_crawling_data(name, title, additional, startDate, link)

#if __name__ == "__main__":
#    holaworld_Crawl()