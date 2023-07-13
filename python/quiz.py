from curses import window
from tabnanny import check
from tracemalloc import start
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from pyparsing import Word
import random
import os

import module.DB.DB_conn as c
conn=c.DBConn.conn


quiz_window= uic.loadUiType("./ui/quiz.ui")[0]

class quiz(QMainWindow, quiz_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #이벤트
        self.OK.clicked.connect(self.ok)
        self.Start.clicked.connect(self.start)
        # 파일 리스트 가져옴
        global path_dir
        global q
        path_dir = '.\module\FlashCards\images'
        file_list = os.listdir(path_dir)
        q=file_list[0::2] # 짝수 리스트 (단어만 가져옴)


    def ok(self):
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
            self.close()
            
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
            




    