import sys
import mariadb


# DB연결 예외 처리

class DBConn:
    try:
        conn = mariadb.connect(
            user="root",
            password="yjh2017E!",
            host="172.30.1.17",
            port=3306,
            database="capston"
        )
        print("연결 성공!")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
