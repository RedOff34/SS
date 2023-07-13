from curses import window
import sys
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sign
import mainFunction
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtWidgets
from qt_material import apply_stylesheet

#DB 모듈 불러오기   
import module.DB.DB_conn as c
conn=c.DBConn.conn


login_window= uic.loadUiType("./ui/login.ui")[0]

        

class MyWindows(QMainWindow, login_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #이벤트
        self.Login_Button.clicked.connect(self.login_buttion)
        self.sign_Button.clicked.connect(self.sign_buttion)

    #로그인 버튼 함수
    def login_buttion(self):
        
        
        id = str(self.ID_textBox.text())
        pw = str(self.PW_textBox.text())
              
        cur = conn.cursor()
        sql = 'select userID, userPassword from USER where userID=%s and userPassword=%s'
        cur.execute(sql,(id,pw))            
        result=cur.fetchall()

        if (id==result[0][0]) and (pw==result[0][1]):
            print("로그인 성공")
            NewUserCal.userID.setID(id)
            
            self.window3=mainFunction.mainFunction()
            self.window3.show()
            self.hide()
        else:
            print("로그인 실패!")

        cur.close()

    #회원 가입 함수
    def sign_buttion(self):
        self.windows2=sign.sign()
        self.windows2.show()
        #self.show()
        



app = QApplication(sys.argv)
window=MyWindows()
window.show()
app.exec_()
