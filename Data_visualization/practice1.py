import matplotlib.pyplot as plt 

x_values = range(1,5)
x2_values = range(1,500)
y_values = [x**3 for x in x_values]
y2_values = [x**3 for x in x2_values]

fig,ax =fig,zx =  plt.subplots()
zx.plot(x_values,y_values,c='red',linewidth = 10)
ax.scatter(x2_values,y2_values,c=y2_values,cmap=plt.cm.Blues,)


plt.show()