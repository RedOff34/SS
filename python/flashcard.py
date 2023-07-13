from curses import window
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
from pyparsing import Word
import module.FlashCards.FlashCards
import module.DB.DB_conn as c
conn=c.DBConn.conn

flashcard_window= uic.loadUiType("./ui/flashcard.ui")[0]

class flashcard(QMainWindow, flashcard_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #이벤트
        self.OK.clicked.connect(self.ok)
        self.Create.clicked.connect(self.create)

    def ok(self):
        self.close()
    
    def create(self):
        Word=str(self.WORD_textBox.text())
        Definition=str(self.DEF_textBox.text())
        module.FlashCards.FlashCards.flashcard(Word,Definition)
        cur = conn.cursor()
        sql = 'insert into flashcard values(%s,%s);'
        cur.execute(sql,(Word,Definition))
        conn.commit()
        QMessageBox.about(self, "생성", "단어 카드가 생성됐습니다.")

        