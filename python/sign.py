from asyncio.windows_events import NULL
from typing_extensions import Self
from PyQt5.QtWidgets import *
from PyQt5 import uic


import module.DB.DB_conn as c
conn=c.DBConn.conn

sign_window= uic.loadUiType("./ui/sign.ui")[0]



class sign(QMainWindow, sign_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #이벤트
        self.Double_Check.clicked.connect(self.double_check)
        self.Nick_Name.clicked.connect(self.nick_name)
        self.Sign_In.clicked.connect(self.sign_in)
    


    def double_check(self):
        id = str(self.ID_textBox.text())
        cur = conn.cursor()
        sql = "select userID from USER where userID=%s"
        cur.execute(sql,(id,))
        result=cur.fetchall()
            
        if not result:
            t = QMessageBox.question(self, "아이디 중복.", "중복된 아이디가 없습니다.", QMessageBox.Yes)
        else:
            f = QMessageBox.question(self, "아이디 중복.", "중복된 아이디입니다.", QMessageBox.Yes)

        
    def nick_name(self):
        NickName = str(self.Nick_Name_textBox.text())
        cur = conn.cursor()
        sql = 'select userName from USER where userName  = %s'
        cur.execute(sql,(NickName,))
        result=cur.fetchall()
        if not result:
            t = QMessageBox.question(self, "닉네임 중복.", "중복된 닉네임이 없습니다.", QMessageBox.Yes)

        else:
            f = QMessageBox.question(self, "닉네임 중복.", "중복된 닉네임입니다.", QMessageBox.Yes)

    def sign_in(self):
        id = str(self.ID_textBox.text())
        pw = str(self.PW_textBox.text())
        NickName = str(self.Nick_Name_textBox.text())
        EmailId = str(self.Email_textBox.text())
        EmailAddress = str(self.Email_comboBox.currentText())
        Email = str(EmailId+EmailAddress)
        gender = str(self.Gender_comboBox.currentText())
        cur = conn.cursor()
        sql = 'insert into USER values(%s,%s,%s,%s,%s);'
        ul=[id,pw,NickName,Email,gender]
        cur.execute(sql,ul)
        conn.commit()
        conn.close()
        ans = QMessageBox.question(self, "환영합니다.", "회원가입이 완료되었습니다.", QMessageBox.Yes)

        if ans == QMessageBox.Yes:
            self.hide()
        
        

