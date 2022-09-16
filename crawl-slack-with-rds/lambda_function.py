from Crawl import Crawl
from DB import TblCrawlingData
from Slack import Slack


def lambda_handler(event, context):
    #crawl = Crawl()
    #crawl.holaworld_Crawl()
    
    slack = Slack()
    slack.toSlack()