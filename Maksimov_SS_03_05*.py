#1
'''
Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). 
Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный. 
Вычисления оформить в виде процедуры.
'''
from random import randint
import math

def finding_angle(x1, x2, y1, y2, z1, z2):
    angle_x = math.atan2(x2, x1)
    angle_y = math.atan2(y2, y1)
    angle_z = math.atan2(z2, z1)
    
    min_angle = min(angle_x, angle_y, angle_z)
    
    if min_angle == angle_x:
        return (x1, x2)
    elif min_angle == angle_y:
        return (y1, y2)
    elif min_angle == angle_z:
        return (z1, z2)

x1, x2 = [randint(1, 15) for x in range(2)]
y1, y2 = [randint(1, 15) for x in range(2)]
z1, z2 = [randint(1, 15) for x in range(2)]

min_angle_point = finding_angle(x1, x2, y1, y2, z1, z2)
print("1 точка: ", x1, x2, "\n" "2 точка: ", y1, y2, "\n" "3 точка: ", z1, z2)
print(min_angle_point) 

#2
'''
Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром, 
т. е. читается одинаково слева направо и справа налево.
'''
def palindromes(n):
    result = []
    for num in range(2, n + 1):
        if is_prime(num) and palindrome_binary(num):
            result.append(num)
    return result

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def palindrome_binary(num):
    binary = format(num, "b")
    return binary == binary[::-1]

n = 999
p = palindromes(n)
print("Все простые натуральные числа, удовлетворяющие условию: ", p)




