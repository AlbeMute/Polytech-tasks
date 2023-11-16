#3
'''
Построить в общих осях графики для x<0.
На том же графике сделать 1 врезку, демонстрирующую поведение графиков при удалении x от 0 к −∞.
Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций. Так же нанесите на графики прямую f(x) = 0.
Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.
'''

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [12, 7]
plt.rcParams['figure.autolayout'] = True

def function(alpha, beta, color):
    x = np.linspace(-10, 0, 999)  
    y = (x ** beta + alpha ** beta) / (x**beta)

    plt.plot(x, y, label=f"\u03b1={alpha}, \u03b2={beta}", color=color)
    plt.axhline(y=0, color='black', linestyle='-', )

function(1, 1, 'r')
function(2, 1, 'g')
function(1, 2, 'b')

plt.plot()
plt.ylim(-15, 15)
plt.xlim(-4, 0)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Графики f(x)')
plt.grid(True)
plt.legend(loc='upper left')



plt.subplot(8, 8, (11, 20))
function(1, 1, 'r')
function(2, 1, 'g')
function(1, 2, 'b')
plt.ylim(-0.6, 1.5)
plt.xlim(-10, -7)
plt.title('Для x → −∞')

plt.show()

#4
'''
Построить в общих осях графики для:
- a=1,β=0.5
- a=1,β=-0.5
- a=1,β=-1.5  
Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость

В результате выполнения предыдущей задачи, вы вероятно заметите, что все графики с
a=1 проходят через общую точку (1, 2).

Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.

Каждый график будет содержать 4 кривые. 2 общих:
- a=1,β=0 (в качестве цвета попробуйте использовать 'b--')
- a=1,β=-1 (в качестве цвета попробуйте использовать 'r--')  
И по 2 уникальных для каждого графика:
- a=1,β=0.5 и
- a=1,β=0.8
- a=1,β=-0.5 и
- a=1,β=-0.8
- a=1,β=-1.5 и
- a=1,β=-2.5
'''

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [12, 7]
plt.rcParams['figure.autolayout'] = True

def function(alpha, beta, color):
    x = np.linspace(-10, 10, 999)  
    y = (x ** beta + alpha ** beta) / (x**beta)

    plt.plot(x, y, label=f"\u03b1={alpha}, \u03b2={beta}", color=color)
   

function(1, 0.5, 'r') # По графику: убывает, вогнутый
function(1, -0.5, 'g') # По графику: возрастает, выпуклый вверх
function(1, -1.5, 'b') # По графику: возрастает, выпуклый вниз

plt.plot()
plt.ylim(-30, 30)
plt.xlim(-4, 10)    
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Графики f(x)')
plt.grid(True)
plt.legend(loc='upper left')

plt.show()


plt.rcParams['figure.figsize'] = [18, 6]
plt.rcParams['figure.autolayout'] = True

def function(alpha, beta, color, linestyle='-'):
    x = np.linspace(-10, 10, 999)  
    y = (x**alpha) / (x**beta)

    plt.plot(x, y, label=f"\u03b1={alpha}, \u03b2={beta}", color=color, linestyle=linestyle)

plt.subplot(1, 3, 1)
function(1, 0, 'b', linestyle='--')
function(1, 0.5, 'b')
function(1, 0.8, 'g')
function(1, -1, 'r', linestyle='--')
plt.ylim(-10, 10)
plt.xlim(-10, 10)    
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('a=1')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 2)
function(1, 0, 'b', linestyle='--')
function(1, -0.5, 'b')
function(1, -0.8, 'g')
function(1, -1, 'r', linestyle='--')
plt.ylim(-10, 10)
plt.xlim(-10, 10)    
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('a=1')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 3)
function(1, 0, 'b', linestyle='--')
function(1, -1.5, 'b')
function(1, -2.5, 'g')
function(1, -1, 'r', linestyle='--')
plt.ylim(-10, 10)
plt.xlim(-10, 10)    
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('a=1')
plt.grid(True)
plt.legend()

plt.suptitle('Графики f(x) для a=1', fontsize=16)
plt.show()