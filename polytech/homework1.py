import math

#1. Вычислить и вывести на экран длину окружности и площадь круга одного и того же заданного радиуса R...
R = float(input("Введите радиус: "))
C = round(2 * math.pi * R, 2)
S = round(math.pi * R**2, 2)
print(C)
print(S)

#2. Даны две переменные x = 10 и y = 55...
x = 10
y = 55
print(x, y)
x, y = y, x
print(x, y)

#3. Вычислить и вывести на экран период колебания маятника длиной L с точностью до сотых...
g = 9.81
L = float(input("Введите длину маятника: "))
T = round(2 * math.pi * math.sqrt(L/g), 2)
print(T)