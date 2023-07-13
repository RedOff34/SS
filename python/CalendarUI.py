from asyncio.windows_events import NULL
from curses import window
import sys
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import *

import NewUserCal
import notion_api



#사용자별 URL 받기
class Urlclss:
    def __init__(self):
        self.url=''

    @classmethod
    def setUrl(self,urlDBID):
        str=notion_api.find_UserDBid(urlDBID)
        new_str=str.replace('-','')
        url="https://smiling-woodwind-4cf.notion.site/"+new_str
        self.url=url


Calui= uic.loadUiType("./ui/Calendar_notion.ui")[0]
#UI 부분
class calendarUI(QMainWindow,Calui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.webEngineView.load(QUrl(Urlclss.url))
        
        self.Create_button.clicked.connect(self.create)
        self.Update_button.clicked.connect(self.update)
        self.Delete_button.clicked.connect(self.delete)
        self.webEngineView.reload() 
        

    #생성 
    def create(self):
        Title = self.Title_text.text()
        Content= self.Content_Text.text()
        selDate=self.Date_set.selectedDate().toString("yyyy-MM-dd")
        notion_api.createvalue(notion_api.find_UserDBid(NewUserCal.userID.id), notion_api.page_header,Title,Content,selDate)
        self.webEngineView.reload() 

    #수정
    def update(self):
                
        oldTitle=self.OldTitle.text()
        NewTitle = self.NewTitle.text()
        Content= self.NewContent_Text.text()
        selDate=self.Date_set.selectedDate().toString("yyyy-MM-dd")
        notion_api.updateValue( notion_api.find_valueID(notion_api.find_UserDBid(NewUserCal.userID.id), notion_api.page_header, oldTitle) ,
        notion_api.page_header, NewTitle,Content,selDate)
        self.webEngineView.reload() 
    
    #삭제
    def delete(self):
        DeleteTitle=self.DeleteTitle.text()
        notion_api.deletevalue(notion_api.find_valueID(notion_api.find_UserDBid(NewUserCal.userID.id), notion_api.page_header, DeleteTitle), notion_api.page_header)
        self.webEngineView.reload() 