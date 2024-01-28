import matplotlib.pyplot as plt 
from Random_walk import RandomWalk
# 创建一个randomWalk实例
while True:
    rw = RandomWalk()
    rw.fill_walk()
    #将所有的点绘制出来
    # plt.style.use('calssic')
    fig,ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values,rw.y_values,linewidth= 0.5,)
    # 突出起点和终点
    ax.scatter(0,0,c='green',edgecolors = 'none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors = 'none',s = 100)
    # ax.axis([0,10000,0,10000])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break