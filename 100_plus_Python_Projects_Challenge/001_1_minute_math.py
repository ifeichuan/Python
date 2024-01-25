import time
import random

def opera(a,b):
    list = ['+','-','*','/']
    operator = random.choice(list)
    print(f"{a} {operator} {b} = ?")
    if operator =='+':
        operator = a+b
    elif operator == '-':
        operator = a-b
    elif operator == '*':
        operator = a*b
    
    else:
        try:
            operator = a/b
        except ZeroDivisionError:
            print("除数不能为0")
            return 0 
    return operator



starttime = time.time()
endtime = time.time()
countTimes = 0
countRight = 0
while (endtime-starttime)<=30:
    countTimes +=1
    a = random.randint(0,100)
    b = random.randint(0,100)
    operation = int(opera(a,b))
    x = int(input("请输入答案:\n"))
    if x == operation:
        countRight+=1
    print(f"剩余时间{30- (int(endtime-starttime))}秒")
    endtime = time.time()
print(f"count = {countTimes},Right = {countRight}\n Correct rate is {(countRight/countTimes)*100}%")


