from curses import window
import sys
from time import sleep
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
import CalendarUI
import notion_api
import time
import CalendarUI

#캘린더 ui에 사용할 사용자 id 클래스
class userID():  

    def __init__(self):
        self.id=''
    @classmethod
    def setID(self,id):
        self.id=id

NewUserCal= uic.loadUiType("./ui/NewUserCal.ui")[0]

class newucal(QMainWindow,NewUserCal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.Yes_Bt.clicked.connect(self.yes_butdon)

    #확인버튼 실행 함수
    def yes_butdon(self):
        #print(type(userID.id))
        notion_api.CreateRootDB(notion_api.parent_pageID,notion_api.page_header,userID.id)
        self.close()

        #사용자 id 전달
        CalendarUI.Urlclss.setUrl(userID.id)
        self.calUI=CalendarUI.calendarUI()
        