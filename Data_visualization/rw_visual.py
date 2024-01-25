import matplotlib.pyplot as plt 
from Random_walk import RandomWalk
# 创建一个randomWalk实例
rw = RandomWalk()
rw.fill_walk()
#将所有的点绘制出来
# plt.style.use('calssic')
fig,ax = plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s = 15)
plt.show()