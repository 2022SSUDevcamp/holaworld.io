import json
import requests
from DB import TblCrawlingData
from DB import Repo
from datetime import datetime

class Slack:

    def toSlack(self):
        repo = Repo()

        #client = slack_sdk.WebClient(token=SLACK_TOKEN)
        message = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초\n")
        message += '지난 한 주의 스터디 목록입니다 : \n\n'

        slack_webhook_url = 'https://#slack-webhook-endpoint'
        headers = {
            "Content-type": "application/json"
        }        

        

        # id , name , content , additional , startDate , link

        # 스터디
        list = repo.get_crawling_data('Study', 3, 4)
        # print("Current date : ", datetime.now())
        for datum in list: # datum : TblCrawlingData 객체
            message += '[스터디 '
            langs = datum.additional.split('&')
            for lang in langs:
                message += f'#{lang} '

            date = datum.startDate.strftime('%Y-%m-%d')
            message += f'] ({date})\n'        
            message += datum.content
            message += '\n'
            #print("link : ", datum.link , " , name : ", datum.name)
            message += f'Link : https://holaworld.io/{datum.name.lower()}/{datum.link}\n\n'

            data = {
            "text" : message
            }

        message += "-----------------------------\n"
        message += "추가 정보 : https://holaworld.io"

        data = {
            "text" : message
        }
        res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
        print(res.status_code)

        message = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초\n")
        message += '지난 한 주의 프로젝트 목록입니다 : \n\n'

        # Project
        list = repo.get_crawling_data('Project', 3, 4)
        for datum in list: # datum : TblCrawlingData 객체
            message += '[프로젝트 '
            langs = datum.additional.split('&')
            for lang in langs:
                message += f'#{lang} '

            date = datum.startDate.strftime('%Y-%m-%d')
            message += f'] ({date})\n'        
            message += datum.content
            message += '\n'
            #print("link : ", datum.link , " , name : ", datum.name)
            message += f'Link : https://holaworld.io/study/{datum.link}\n\n'

        message += "-----------------------------\n"
        message += "추가 정보 : https://holaworld.io"

        data = {
            "text" : message
        }
        res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
        print(res.status_code)    
            





            

        #client = slack_sdk.WebClient(token=SLACK_TOKEN)
        #client.chat_postMessage(channel=SLACK_CHANNEL, text=message)


#if __name__ #== "__main__":
#    toSlack()