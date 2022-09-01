import requests
import json
from sqlalchemy import create_engine, text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry, Session 
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
engine = create_engine(
    "mysql+pymysql://username:password@localhost:3306/project_?charset=utf8mb4",
    echo=True,
    future=True,
)

# SQL문
# -- auto-generated definition
# CREATE TABLE tbl_crawling_data
# (
#   id      int AUTO_INCREMENT
#     PRIMARY KEY,
#   name    varchar(255)  NULL,
#   content varchar(1024) NULL
# );

############# 여기까지 OK

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry, Session  

# id : 프로젝트 Serial No
        # name : 모집 종류 / 프로젝트(1) / 스터디(2) / 모집됨(0)
        # content : 텍스트
        # additional : 언어 리스트
        # startDate : 시작 예정일

# NameError: name 'Base' is not defined
# class 클래스이름(상속클래스):
class TblCrawlingData(Base):
    __tablename__ = "tbl_crawling_data"

    # id는 Base 클래스에 정의되어 있다.
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    content = Column(String(1024))
    additional = Column(String(1024))
    startDate = datetime

    def __init__(self, name, content, additional, startDate):
        self.name = name
        self.content = content
        self.additional = additional
        self.startDate = startDate

    # 객체를 문자열로 반환하는 함수
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, content={self.content!r}, additional={self.additional!r}, startDate={self.additional!r})"

# 에러 발생
# sqlalchemy.orm.exc.UnmappedInstanceError: Class 'temp_DB.TblCrawlingData' is not mapped


# -- 코드를 하나로 모으면 좋은 이유 ---
class Repo(object):
    def __init__(self):
        self.engine = create_engine(
            # mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
            "mysql+pymysql://username:password@localhost:3306/project_?charset=utf8mb4",
            echo=True,
            future=True,
        )

        self.mapper_registry = registry()
        self.Base = self.mapper_registry.generate_base()

        self.session = Session(self.engine)

# id , name , content , additional , startDate

    def add_crawling_data(self, name: str, content: str, additional: str, startDate:datetime):
        self.session.add(TblCrawlingData(name=name, content=content, additional=additional, startDate=startDate))
        self.session.commit()

    def get_crawling_data(self, name: str):
        query = self.session.query(TblCrawlingData)
        query = query.filter(TblCrawlingData.name == name)
        return query.all()
