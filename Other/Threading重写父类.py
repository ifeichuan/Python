import threading
import time 
from time import sleep

class myThread(threading.Thread):
    # task为传递的函数名称
    def __init__(self,number,letter,task):
        threading.Thread.__init__(self)
        self.number = number
        self.letter = letter
        self.daemon = False

    def run(self):
        print(f"[线程开始] {self.name}")
        task(self.name,self.number,self.letter)
        print(f"[线程结束] {self.name}")
    
    def __del__(self):
        print("[线程销毁释放内存]",self.name)

def task(threadName, number, letter):
    m = 0
    while m < number:
        sleep(1)
        m += 1
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{current_time}] {threadName} 输出 {letter}")


myThread1 = myThread(4,'a',task=task)
myThread2 = myThread(task=task,number=5,letter='CS')

myThread1.start()
myThread2.start()
# 当daemon参数为True时,若主程序执行完毕(即不包括Thread这部分),而还有线程未执行完毕,会强行结束
myThread2.join()
# time.sleep(4)


