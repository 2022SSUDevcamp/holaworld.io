import requests
import json
from DB import TblCrawlingData
from DB import Repo
from datetime import datetime

class Crawl:

    def holaworld_Crawl(self):

        repo = Repo()
        study = repo.get_crawling_data('Study', 365, 365) # 전체 다 가져오기
        study_cur = study[0].link # link-id는 증가순이니까 최근 것만 보면 됨( 문자열 순서 비교 ) , 최근 생성된 것의 id
        #print(study_cur)
        current = study_cur

        project_cur = repo.get_crawling_data('Project', 365, 365) # 전체 다 가져오기
        project_cur = project_cur[0].link # 최근 생성된 것의 id
        #print(project_cur)
        if project_cur > current:
            current = project_cur

        # limit만 내가 수정해서 크롤링 하면 된다.
        url = "https://api.holaworld.io/api/posts?sort=-createdAt&offset=0&limit=1000&isClosed=false&type=0"
        response = requests.get(url)
        data = json.loads(response.text)

        list = []
        
        for datum in data:
            
            # language = 언어 리스트
            # isClosed = boolean 값
            # startDate = '2022-09-04T15:16:00.000Z'
            # endDate : 없는 듯
            # comments = 댓글 딕셔너리 리스트
            # id = 스터디에 지정된 id primary key 값

            # print(datum.keys()) # 각 항목의 key를 얻을 수 있다.

            # 링크 = holaworld.io/study혹은project/id명 - name 변수를 lower() 처리하여 조합해야 함
            link = datum.get('id')# 일단 id만 저장하고 , 나중에 불러올 때 링크를 조합할 예정
            if link < current: # 이미 가져온 데이터라면 넣지 데이터베이스에 넣지 않는다.
                continue

            # additional : 사용할 언어 / 프레임워크
            langs = datum.get("language")
            additional = '&'.join(langs)
            # print( datum.get('type')) # 

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

            list.append(TblCrawlingData(name, content, additional, startDate, link))
            
        repo.add_crawling_data(list)