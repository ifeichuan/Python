from threading import Thread
import time
from time import sleep


# Newthread = Thread(target=function,args=(argument1,....))
# Newthread 创建的线程对象
#  function 要执行的函数 

def task(threadName,number,letter):
    print(f"线程开始{threadName}")
    m = 0
    while m < number:
        sleep(1)
        m += 1
        current_time = time.strftime('%H:%M:%S',time.localtime())
        print(f"[{current_time}] {threadName} 输出 {letter}\n")
    print(f"线程结束 {threadName}")

# 线程1 执行任务打印4个a
thread1 = Thread(target=task,args=("thread_1",4,"a"))
# 线程2 执行任务打印2个ccc
thread2 = Thread(target=task,args=("thread_2",6,"cccc"))
thread3 = Thread(target=task,args=("thread_3",2,"Dog"))

thread1.start()
thread2.start()
thread1.join()
# thread3.start()

thread2.join()
# 启动取决于上一个阻塞,若在thread1.join()后启动,则会和thread2并发执行
thread3.start()
thread3.join()






