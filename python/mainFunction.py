from asyncio.windows_events import NULL
from curses import window
import sys
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import module.Tesseract_ocr.convert
import module.anyang_video.anyang_videoUrl
import module.FlashCards.FlashCards
import module.youtube_download.youtube_download
import module.video2pdfslides.video2pdfslides

import NewUserCal
import notion_api
import CalendarUI
import random
from pyparsing import Word
import os
import webbrowser



#DB 모듈 불러오기
import module.DB.DB_conn as c
conn=c.DBConn.conn


mainFunction_window= uic.loadUiType("./ui/mainFunction.ui")[0]



class mainFunction(QMainWindow, mainFunction_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.youtube.clicked.connect(self.buttonClick)
        self.anyang.clicked.connect(self.buttonClick)
        self.pdf.clicked.connect(self.buttonClick)
        self.ocr.clicked.connect(self.buttonClick)
        self.calendar.clicked.connect(self.buttonClick)
        self.flashcard.clicked.connect(self.buttonClick)
        self.quiz.clicked.connect(self.buttonClick)
        self.bbs.clicked.connect(lambda: webbrowser.open('http://172.30.1.17/main.jsp'))
        # 위젯 버튼
        self.OK.clicked.connect(self.ok) # 안양대학교 확인 버튼
        self.Home.clicked.connect(self.home) # 안양대학교 홈페이지 
        self.OK_2.clicked.connect(self.u_ok) # 유튜브 다운로드
        self.OK_3.clicked.connect(self.p_ok) # pdf 추출
        self.Create.clicked.connect(self.create) # 단어 카드 생성
        self.OK_5.clicked.connect(self.q_ok) # 단어 확인
        self.Start.clicked.connect(self.start) # 문제 시작
        global path_dir
        global q
        path_dir = '.\module\FlashCards\images'
        file_list = os.listdir(path_dir)
        q=file_list[0::2] # 짝수 리스트 (단어만 가져옴)
        
        self.stackedWidget:QStackedWidget # class type 지정해주기
        self.stackedWidget.setCurrentIndex(0)

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if  btnName == "anyang":
            
            self.stackedWidget.setCurrentIndex(1)
            # self.windows3=anyangvideo.anyangvideo()
            # self.windows3.show()
        elif btnName == "youtube":
            self.stackedWidget.setCurrentIndex(2)
            # self.window2=youtube.youtube()
            # self.window2.show()
        elif btnName =="pdf":
            self.stackedWidget.setCurrentIndex(3)
            # self.window4=pdf.video()
            # self.window4.show()
        elif btnName == "ocr":
            module.Tesseract_ocr.convert.pdf_to_ocr()
        elif btnName == "calendar":
            #유저별 캘린더 생성 여부 검증
            if notion_api.find_UserDBid(NewUserCal.userID.id)=='':
                self.CalWin=NewUserCal.newucal()
                
            else:
                #사용자 id 전달
                CalendarUI.Urlclss.setUrl(NewUserCal.userID.id)
                self.calUI=CalendarUI.calendarUI()

        elif btnName == "flashcard":
            self.stackedWidget.setCurrentIndex(4)
            # self.window5=flashcard.flashcard()
            # self.window5.show()
        elif btnName == "quiz":
            self.stackedWidget.setCurrentIndex(5)

            # self.window6=quiz.quiz()
            # self.window6.show()

    # 안양대학교 동영상 다운로드
    def home(self):
        module.anyang_video.anyang_videoUrl.anyang_url()
    def ok(self):
        module.anyang_video.anyang_videoUrl.anyang_down()
    # 유튜브 동영상 다운로드
    def u_ok(self):
        
        url=str(self.URL_textBox.text())
        module.youtube_download.youtube_download.youtube_down(url)
    # pdf 추출
    def p_ok(self):
        video_path=str(self.Video_textBox.text())
        module.video2pdfslides.video2pdfslides.video2pdfslides(video_path)


    def create(self):
        Word=str(self.WORD_textBox.text())
        Definition=str(self.DEF_textBox.text())
        module.FlashCards.FlashCards.flashcard(Word,Definition)
        cur = conn.cursor()
        sql = 'insert into flashcard values(%s,%s);'
        cur.execute(sql,(Word,Definition))
        conn.commit()
        QMessageBox.about(self, "생성", "단어 카드가 생성됐습니다.")
    
    # 단어 퀴즈
    def q_ok(self):
        global ck
        ck = False
        Answer=str(self.Answer_textBox.text())
        cur = conn.cursor()
        sql = 'select * from flashcard where wordExplain=%s;'
        cur.execute(sql,(n,))
        result=cur.fetchall()
        if Answer==result[0][1]:
            a = QMessageBox.question(self, "정답", "정답입니다!".format(result[0][1]), QMessageBox.Yes)
            if a == QMessageBox.Yes:
                self.start()
        else:
            a = QMessageBox.question(self, "오답", "오답입니다! 정답은 {}!".format(result[0][1]), QMessageBox.Yes)
            if a == QMessageBox.Yes:
                self.start()
    
    def start(self):
        if not q: # 문제가 없을때
            QMessageBox.about(self, "오류", "문제가 없습니다.!")

            
        else: # 문제가 있을때
            r=random.randint(0,len(q)-1)

            # 가져올 이미지의 이름
            img_name = path_dir + '\\' + q[r]
            global n
            n = q[r][:-4]
            print("n="+n)

            #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load("{}".format(img_name))
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
            self.Picture.setPixmap(self.qPixmapFileVar)
            q.pop(r)
    
'''
app = QApplication(sys.argv)
window=mainFuntion()
window.show()
app.exec_()
'''