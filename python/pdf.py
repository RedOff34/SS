from curses import window
import sys
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
import module.video2pdfslides.video2pdfslides

import sign
import mainFunction

#DB 모듈 불러오기
import module.DB.DB_conn as c
conn=c.DBConn.conn

video_window= uic.loadUiType("./ui/pdf.ui")[0]

class video(QMainWindow, video_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #이벤트
        self.OK.clicked.connect(self.ok)

    def ok(self):
        video_path=str(self.Video_textBox.text())
        module.video2pdfslides.video2pdfslides.video2pdfslides(video_path)
        self.close()