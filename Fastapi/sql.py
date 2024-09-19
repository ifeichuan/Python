import pymysql


db = pymysql.connect(
    host="localhost",
    user='root',
    password='root',
    database='test'
                     )

cursor = db.cursor()

cursor.execute(f"select userinfo.username from userinfo where 'Feichuan' = userinfo.username")
data = cursor.fetchone()
print(data[0])
if(data[0]=='Feichuan'):
    print(1)