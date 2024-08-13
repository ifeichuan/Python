"""
<case5: 线程同步，线程锁>
Date: 2024/5/15
Author: 猫猫不吃sakana
"""
 
import threading
import time
 
 
# 子类myThread继承父类threading.Thread，并进行重写
class myThread(threading.Thread):
    # 重写父类构造函数
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number
 
    # 重写父类run函数，在调用start()时自动调用run函数
    def run(self):
        print(f"【线程开始】{self.name}")
        Lock.acquire()  # 设置线程锁
        edit_list(self.name, self.number)
        Lock.release()  # 释放线程锁
 
    # 重写父类析构函数
    def __del__(self):
        print("【线程销毁】", self.name)
 
 
# 自定义的任务函数
def edit_list(threadName, number):
    while number > 0:
        time.sleep(1)
        data_list[number-1] += 1
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{current_time}] {threadName} 修改datalist为{data_list}")
        number -= 1
    print(f"【线程{threadName}完成工作】")
 
 
data_list = [0, 0, 0, 0,0,0,0,0,0]
Lock = threading.Lock()
 
# 创建3个子线程
thread1 = myThread(3)
thread2 = myThread(6)
thread3 = myThread(5)
 
# 启动3个子线程
thread1.start()
thread2.start()
thread3.start()
 
# 主进程等待所有线程完成
thread1.join()
thread2.join()
thread3.join()
 
print("【主进程结束】")