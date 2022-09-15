from Slack import Slack
import json # 파이썬 기본 라이브러리
import urllib.request # 파이썬 기본 라이브러리

def post_slack(argStr):
    message = argStr
    send_data = {
        "text": message,
    }
    send_text = json.dumps(send_data)
    request = urllib.request.Request(
        "https://hooks.slack.com/services/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", 
        data=send_text.encode('utf-8'), 
    )

    with urllib.request.urlopen(request) as response:
        slack_message = response.read()

def lambda_handler(event, context):
#if __name__ == '__main__':
    slack = Slack()
    message = slack.studyToSlack()
    post_slack(message)