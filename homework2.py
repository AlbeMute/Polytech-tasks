#1
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if b != 0:
    y = a/b
else:
    y = "Error"
print(y)

#2
# m - общая сумма покупки
# d - скидка
# r - размер скидки
s = float(input("Введите сумму покупки: "))
d = 0.35
if s > 20:
    m = s*0.65
    r = s - m
    print("Итоговая сумма покупки: ", round(m, 2), "Размер скидки: ", round(r, 2))
else:
    print("Скидка не предоставлена.", "Итоговая сумма покупки: ", round(s, 2))
          
#3
a = int(input("Введите число от 1 до 12: "))
if a == 1:
    print("Январь - Зима")
elif a == 2:
    print("Февраль - Зима")
elif a == 3:
    print("Март - Весна")
elif a == 4:
    print("Апрель - Весна")
elif a == 5:
    print("Май - Весна")
elif a == 6:
    print("Июнь - Лето")
elif a == 7:
    print("Июль - Лето")
elif a == 8:
    print("Август - Лето")
elif a == 9:
    print("Сентябрь - Осень")
elif a == 10:
    print("Октябрь - Осень")
elif a == 11:
    print("Ноябрь - Осень")
elif a == 12:
    print("Декабрь - Зима")
else:
    print("Ошибка: Введите число от 1 до 12!")

import math
a = int(input())
b = int(input())
c = int(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = ((-1) * b + math.sqrt(d)) / (2 * a)
    x2 = ((-1) * b - math.sqrt(d)) / (2 * a)
    print(d, x1, x2)
elif d == 0:
    x = ((-1) * b) / (2 * a)
    print(d, x)
else:
    print("Корней нет")
