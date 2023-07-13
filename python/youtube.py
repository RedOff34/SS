from curses import window
import sys
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
import module.youtube_download.youtube_download

import sign
import mainFunction

#DB 모듈 불러오기
import module.DB.DB_conn as c
conn=c.DBConn.conn


youtube_window= uic.loadUiType("./ui/youtube.ui")[0]

class youtube(QMainWindow, youtube_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #이벤트
        self.OK.clicked.connect(self.ok)

    def ok(self):
        url=str(self.URL_textBox.text())
        module.youtube_download.youtube_download.youtube_down(url)
        self.close()


