import slack_sdk
import json
from DB import Repo
from DB import TblCrawlingData
from datetime import datetime

if __name__ == '__main__':
    SLACK_TOKEN = '#SLACKBOT_oAUTH_TOKEN' # 사용할 때는 이 부분( 메세지를 보낼 BOT Serial NO ) 수정해서 사용한다.
    SLACK_CHANNEL = '#msgfrombot2' # 사용할 때는 이 부분( 메세지가 도착할 채널명 ) 수정해서 사용한다.
    repo = Repo()
    
    today = datetime.now()
    client = slack_sdk.WebClient(token=SLACK_TOKEN)
    message = '지난 한 주의 스터디 목록입니다 : \n\n'

    # id , name , content , additional , startDate , link

    # 스터디
    # print("Current date : ", datetime.now())
    data = repo.get_crawling_data('Study')
    for datum in data: # datum : TblCrawlingData 객체
        message += '[스터디 '
        langs = datum.additional.split('&')
        for lang in langs:
            message += f'#{lang} '

        date = datum.startDate.strftime('%Y-%m-%d')
        message += f'] ({date})\n'        
        message += datum.content
        message += '\n'
        message += f'Link : https://holaworld.io/{datum.name.lower()}/{datum.link}\n\n'
    message += "-----------------------------\n"
    message += "추가 정보 : https://holaworld.io"
    client.chat_postMessage(channel=SLACK_CHANNEL, text=message)

    # 프로젝트
    message = '지난 한 주의 프로젝트 목록입니다 : \n\n'
    # print("Current date : ", datetime.now())
    data = repo.get_crawling_data('Project')
    for datum in data: # datum : TblCrawlingData 객체
        message += '[프로젝트 '
        langs = datum.additional.split('&')
        for lang in langs:
            message += f'#{lang} '

        date = datum.startDate.strftime('%Y-%m-%d')
        message += f'] ({date})\n'        
        message += datum.content
        message += '\n'
        message += f'Link : https://holaworld.io/study/{datum.link}\n\n'
    message += "-----------------------------\n"
    message += "추가 정보 : https://holaworld.io"
    client.chat_postMessage(channel=SLACK_CHANNEL, text=message)

    #client = slack_sdk.WebClient(token=SLACK_TOKEN)
    #client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
