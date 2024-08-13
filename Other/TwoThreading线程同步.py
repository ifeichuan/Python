import threading 
import time 
from time import sleep
str = ['a']
Lock = threading.Lock()
def changeStr(threadName,str):
    current_time = time.strftime("%H:%M:%S",time.localtime())
    i = 0
    # Lock.acquire()
    if len(str)%2==0:
        x = 'c'
    else:
        x = 'D'
    print(f"x = {x} strlen = {len(str)}")
    
    while(i<len(str)):
        sleep(1)
        str[i] += x
        print(f"[{current_time}] {threadName} 修改 str 为 {str}\n")
        i += 1
    str.append('b')
    print(f"{current_time} {threadName} 线程结束")
    # Lock.release()


thread1 = threading.Thread(target=changeStr,args=("thread1",str))
thread2 = threading.Thread(target=changeStr,args=("thread2",str))
thread3 = threading.Thread(target=changeStr,args=("thread3",str))
thread4 = threading.Thread(target=changeStr,args=("thread4",str))
thread1.start()
thread2.start()
thread3.start()
thread3.join()
thread4.start()




