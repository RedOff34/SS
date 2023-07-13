from curses import window
import sys
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
import module.anyang_video.anyang_videoUrl

import sign
import mainFunction

#DB 모듈 불러오기
import module.DB.DB_conn as c
conn=c.DBConn.conn

global ok
ok=0

anyangvideo_window= uic.loadUiType("./ui/anyangvideo.ui")[0]

class anyangvideo(QMainWindow, anyangvideo_window):

    btn=0
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.show()

        #이벤트
        self.OK.clicked.connect(self.ok)
        self.Home.clicked.connect(self.home)
    
   
    def home(self):
        module.anyang_video.anyang_videoUrl.anyang_url()
        
        
    def ok(self):
        module.anyang_video.anyang_videoUrl.anyang_down()

