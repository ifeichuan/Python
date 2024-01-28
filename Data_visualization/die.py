from random import randint

class Die:
    """表示一个骰子的类"""
    def __init__(self,num_sides=6) -> None:
        """默认为六面"""
        self.num_sides = num_sides

    def roll(self):
        """返回1~6之间的数"""
        return randint(1,self.num_sides)