#1
'''
Для каждой задачи необходимо:

- Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций), график каждой функции должен быть одного цвета для одного значения α и β.
- Подписать оси и заголовок
- Создать легенду
- Сохранить изображение в svg файл
1. Построить в общих осях графики для:
- a=1,b=1
- a=2,b=1
- a=1,b=2
'''
from matplotlib import pyplot as plt
import numpy as np

def function(alpha, beta, color):
    x1 = np.linspace(-4, -0.01, 100)  
    y1 = (x1 ** beta + alpha ** beta) / (x1**beta)

    x2 = np.linspace(0.01, 4, 100)
    y2 = (x2 ** beta + alpha ** beta) / (x2**beta)
    
    plt.plot(x1, y1, color=color)
    plt.plot(x2, y2, color=color)

    plt.plot(x1, y1, label=f"\u03b1={alpha}, \u03b2={beta}", color=color)

function(1, 1, 'r')
function(2, 1, 'g')
function(1, 2, 'b')

plt.ylim(-30, 50)
plt.xlim(-4, 4)
plt.xlabel('Ось х')
plt.ylabel('Ось у')
plt.title('График функции f(x)')
plt.legend()
plt.grid(True)
plt.savefig("plot.svg")
plt.show()

#2
'''
Построить в общих осях графики для x>0.
На том же графике сделать 2 врезки, демонстрирующие поведение графиков на 2 интервалах:

- для малых x
- для больших x

Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций.
Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.
'''
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [12, 7]
plt.rcParams['figure.autolayout'] = True

def function(alpha, beta, color):
    x = np.linspace(0, 10, 999)  
    y = (x ** beta + alpha ** beta) / (x**beta)

    plt.plot(x, y, label=f"\u03b1={alpha}, \u03b2={beta}", color=color)

function(1, 1, 'r')
function(2, 1, 'g')
function(1, 2, 'b')

plt.ylim(0, 30)
plt.xlim(0, 5)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Графики f(x)')
plt.grid(True)
plt.legend(loc='upper right')

plt.subplot(3, 4, 7)
function(1, 1, 'r')
function(2, 1, 'g')
function(1, 2, 'b')
plt.ylim(0.5, 1.5)
plt.xlim(7, 10)
plt.title('Для больших х')

plt.subplot(3, 4, 6)
function(1, 1, 'r')
function(2, 1, 'g')
function(1, 2, 'b')
plt.ylim(7, 12)
plt.xlim(0, 0.5)
plt.title('Для малых х')

plt.show()


































