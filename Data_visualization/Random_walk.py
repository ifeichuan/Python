from random import choice

class RandomWalk:
    """一个生成随机漫步的类"""

    def __init__(self,num_points=5000) -> None:
        """初始化随机漫步属性"""
        self.num_points = num_points

        #所有随机漫步始于(0,0)
        self.x_values = [0,]
        self.y_values = [0,]

def fill_walk(self):
    """计算漫步包含的所有点"""
    #不断漫步，直到列表达到指定的长度
    while len(self.x_values)