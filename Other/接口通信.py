from flask import Flask,request,redirect
import pymysql
import pymysql.err
# app = Flask(__name__)
# @app.route('/login/<username>&<password>')
# def login(username,password):

#     return "年后" + username+password

# if __name__ == "__main__":
#     app.run()

db= pymysql.connect(host='localhost',user='root',passwd='root',database='test')
# 创建一个游标对象
cursor = db.cursor()
cursor.execute("select * from 用户")
data = cursor.fetchall()
print(data[-1])

try:
    cursor.execute("insert into 用户 values(2,'scnx','xdnmvsas')")
    db.commit()
except pymysql.err.DatabaseError:
    print("数据错误")
    db.rollback()
except pymysql.err.IntegrityError:
    print('完整性错误')
    db.rollback()
print(cursor.fetchall())
request.form