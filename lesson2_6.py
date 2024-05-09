'''Написать программу для вычисления производной и построения графика от функции e^(a)^x'''

import math
from matplotlib import pyplot as plt  
import numpy as np

class Derivate:
    def __init__(self, func):
        self.__fn = func
   
    def __call__(self, a, x, dx= 0.0001):
        return(self.__fn(a, x + dx) - self.__fn(a, x))/ dx

class Plot_the_chart:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, x):
        x = np.linspace(-4, 5, 80)
        y = self.func(a, x)

        plt.plot(x, y)
        plt.grid(True)
        plt.show()

@Plot_the_chart
@Derivate
def df_(a, x):
    return math.e ** (a) ** x
print(df_(2, 3))

# def sin(y):
#     return math.e ** (math.sin(y)) ** x








    

    


