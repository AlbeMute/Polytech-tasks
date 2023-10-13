
#1

#Ввести одномерный массив A длиной m. Поменять в нём местами первый и последний элементы. Длину массива и его элементы ввести с клавиатуры. 
#В программе описать процедуру для замены элементов массива. Вывести исходные и полученные массивы.


from random import randint

def swap(array):
    array[0], array[-1] = array[-1], array[0]
    return array

m = int(input("Введите длину массива: "))
a = [randint(1, 10) for x in range(m)]

print(a)
print(swap(a))


#2

#Даны две дроби A/B и C/D (A, B, C, D - натуральные числа). Составить программу деления дроби на дробь. 
#Ответ должен быть несократимой дробью. Использовать подпрограмму алгоритма Евклида для определения НОД.


def euclidean(a,b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Введите числитель первой дроби: "))
b = int(input("Введите знаменатель первой дроби: "))
c = int(input("Введите числитель второй дроби: "))
d = int(input("Введите знаменатель второй дроби: "))

n = a*d
d = b*c

nod = euclidean(n,d)
s_n = n // nod
s_d = d // nod
print(f"Результат деления: {s_n}/{s_d}")

#3

#Задана окружность `(x-a)^2 + (y-b)^2 = r^2` и точки P(p1, p2), F(f1, f2), L(l1, l2). 
#Выяснить и вывести на экран, сколько точек и какие лежат внутри окружности. Проверку сформировать в виде процедуры.

a = float(input("Введите координату a окружности: "))
b = float(input("Введите координату b окружности: "))
r = float(input("Введите радиус r окружности: "))

p1 = float(input("Введите координату p1 точки P: "))
p2 = float(input("Введите координату p2 точки P: "))
f1 = float(input("Введите координату f1 точки F: "))
f2 = float(input("Введите координату f2 точки F: "))
l1 = float(input("Введите координату l1 точки L: "))
l2 = float(input("Введите координату l2 точки L: "))

def check(x, y, a, b, r):
    distance = (x-a) ** 2 + (y-b) ** 2
    if distance < r ** 2:
        return "Внутри окружности"
    elif distance == r **2:
        return "На окружности"
    else:
        return "Снаружи окружности"
    
p = check(p1, p2, a, b, r)
f = check(f1, f2, a, b, r)
l = check(l1, l2, a, b, r)

print("Точка P лежит", p)
print("Точка F лежит", f)
print("Точка L лежит", l)

count = 0
if p == "Внутри окружности":
    count += 1
if f == "Внутри окружности":
    count += 1
if l == "Внутри окружности":
    count += 1
    
print(count)


#4

#Даны 3 различных массива целых чисел (размер каждого не превышает 15). В каждом массиве найти сумму элементов и среднеарифметическое значение. 
#Массивы сформировать рандомно.

from random import randint

def massive(array):
    sum_elem = sum(array)
    average = sum(array) / len(array)
    return sum_elem, average

a = [randint(1, 15) for x in range(10)]
b = [randint(1, 15) for x in range(8)]
c = [randint(1, 15) for x in range(12)]

print("Первый массив: ", a, "\n" "Второй массив: ", b, "\n" "Третий массив: ", c)
print("У первого массива: ", massive(a), "\n" "У второго массива: ", massive(b), "\n" "У третьего массива: ", massive(c))



#5

#Даны катеты двух прямоугольных треугольников. Написать функцию вычисления длины гипотенузы этих треугольников. 
#Сравнить и вывести какая из гипотенуз больше, а какая меньше. Катеты определить рандомно, вывести.

from random import randint
import math

def hyp(a, b):
    return math.sqrt(a**2 + b**2)  # a, b катеты треугольника

a_1, a_2 = [randint(1, 15) for _ in range(1)], [randint(1, 15) for _ in range(1)]
b_1, b_2 = [randint(1, 15) for _ in range(1)], [randint(1, 15) for _ in range(1)]

hyp_1 = hyp(a_1[0], b_1[0])  
hyp_2 = hyp(a_2[0], b_2[0])  

print("Первый треугольник:")
print(f"Катет 1: {a_1}")
print(f"Катет 2: {b_1}")
print(f"Гипотенуза: {hyp_1}")
print("-----------------------")
print("Второй треугольник:")
print(f"Катет 1: {a_2}")
print(f"Катет 2: {b_2}")
print(f"Гипотенуза: {hyp_2}")
print("-----------------------")

if hyp_1 < hyp_2:
    print("Гипотенуза 2 больше Гипотенузы 1")
elif hyp_2 < hyp_1:
    print("Гипотенуза 1 больше Гипотенузы 2")
else:
    print("Гипотенузы равны")

#6

#Натуральное число, в записи которого n цифр, называется числом Армстронга, если сумма его цифр, возведенная в степень n, равна самому числу. 
#Найти все числа Армстронга от 1 до к.

def armstrong_number(num):
    num_str = str(num)
    num_sum = sum(int(digit)**len(num_str) for digit in num_str)
    return num_sum == num

k = int(input("Введите верхнюю границу диапазона: "))

armstrong_numbers = [num for num in range(1, k+1) if armstrong_number(num)]

print("Числа Армстронга от 1 до", k, ":")
print(armstrong_numbers)




