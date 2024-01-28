from random import choice

class RandomWalk:
    """一个生成随机漫步的类"""

    def __init__(self,num_points=5000) -> None:
        """初始化随机漫步属性"""
        self.num_points = num_points

        #所有随机漫步始于(0,0)
        self.x_values = [0,]
        self.y_values = [0,]
    def get_Step(self):
            #决定前进方向及前进距离
            x_direction  = choice([1,-1])#左右
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])#前后
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            return x_step,y_step
    def fill_walk(self):
        """计算漫步包含的所有点"""
        #不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            x_step,y_step = self.get_Step()

            # 计算下一个点的x值和y值
            x =self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

"""test code"""
# randomwalk = RandomWalk()
# randomwalk.fill_walk()
# for x,y in zip(randomwalk.x_values,randomwalk.y_values):
#     print(f"{x},{y}\n")