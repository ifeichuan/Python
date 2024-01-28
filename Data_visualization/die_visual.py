from plotly.graph_objs import Bar,Layout
from plotly import offline

from die import Die
# while True:
    #创建一个D6（面数）
die_1 = Die()
die_2 = Die(10)
#掷几次骰子并将结果存储在列表中
results = []
for roll_num in range(1000):
    results.append(die_1.roll()+die_2.roll())
    
#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
x_values = list(range(2,max_result+1))
"""Plotly类Bar()表示用于绘制条形图的数据集，接收xy轴的两个列表，必须放在方括号内，因为可能包含多个元素"""
data  = [Bar(x=x_values,y=frequencies)]

# 配置坐标轴，每个配置选项为字典
x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}
# 类Layout()返回一个指定图标布局和配置的对象，这里设定了图表名称，并传入了x轴和y轴的配置字典
my_layout = Layout(title='掷一个D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')
    # keep_running = input("是否继续(y/n)")
    # if keep_running == 'n':
    #     break