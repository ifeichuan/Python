import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rc("font",family='YouYuan')

input_values = range(1,1001)
squares = [x**2 for x in input_values]

plt.style.use('Solarize_Light2')
fig,ax = plt.subplots()
ax.scatter(input_values,squares,s=10,c=input_values,cmap=plt.cm.inferno,linewidth = 1)

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数",fontsize = 24)
ax.set_xlabel("值",fontsize = 14)
ax.set_ylabel("值的平方",fontsize = 14)

#设置每个坐标轴取值范围
ax.axis([0,1001,0,1100000])
# 设置刻度标记的大小
ax.tick_params(axis="both",labelsize = 14)

plt.savefig('scatter.png',bbox_inches = 'tight')
