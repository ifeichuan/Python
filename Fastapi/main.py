from fastapi import FastAPI,HTTPException,Cookie,Header,Request,Response
import uvicorn
from typing import Union
import asyncio
from pydantic import BaseModel
import pymysql
from selfuuid import generateuuid
import jwt


SECRET_KEY = "152051c872ef7b90ab00d372e735948fdd4632240a61751f049c7e3f7c633771"


app = FastAPI()

db = pymysql.connect(
    host="localhost",
    user='root',
    password='root',
    database='test'
                     )

cursor = db.cursor()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_items(item_id:int,q:Union[str,None]=None):
    return {"item_id":item_id,"q":q}

@app.post("/async/")
async def sync():
    nums = []
    with open('./Fastapi/nums.txt','r') as f:
        for line in f:
            nums.append(line[:-1])
    return {"nums":nums}

class userInfo(BaseModel):
    uuid:str = None
    username:str
    password:str 
    tokenJWT:str = None

@app.post("/login")
def login(userInfo:userInfo,response:Response):
    # 第一次登录
    username,password = userInfo.username,userInfo.password
    if(userInfo.tokenJWT == 'string'):
        cursor.execute(f"select username,password from userinfo where userinfo.username = '{username}' and userinfo.password = '{password}'")
        isright = cursor.fetchone()
        print(f"isright = {isright}")
        if(isright is None):
            raise HTTPException(status_code=401,detail="账号或密码错误")
        selectusername= isright[0]
        selectpassword = isright[1]
        selectpayload={
            "username":selectusername,
            "password":selectpassword
        }
        payload={
            "username":username,
            "password":password
        }
        token1 = jwt.encode(selectpayload,SECRET_KEY,algorithm="HS256")
        token2 = jwt.encode(payload,SECRET_KEY,algorithm="HS256")
        if(token1==token2):
            return {"token":token2,"message":"登录成功"}

@app.post("/register")
def register(userInfo:userInfo):
    # 重复密码逻辑由前端进行验证
    username,password = userInfo.username,userInfo.password
    cursor.execute(f"select userinfo.username from userinfo where '{username}' = userinfo.username")
    isregister = cursor.fetchone()
    if(isregister is None):
        try:
            uuid = generateuuid(username)
            cursor.execute(f"insert into userinfo(uuid,username,password) values('{uuid}','{username}','{password}')")
            db.commit()
            # 重定向交给前端
            return {"message":"注册成功"}
        except:
            db.rollback()
    raise HTTPException(status_code = 409,detail="this Nick name Has Already Been Registered")


if __name__ == "__main__":
    uvicorn.run(app="main:app",host="127.0.0.1",port=8000,reload=True)