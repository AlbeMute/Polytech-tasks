import math
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

if 1 <= a <= 12:
    months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    seasons = ["Зима", "Весна", "Лето", "Осень"]

    month_name = months[a - 1]

    if 1 <= a <= 2 or a == 12:
        season_name = seasons[0] # Зима
    elif 3 <= a <= 5:
        season_name = seasons[1] # Весна
    elif 6 <= a <= 8:
        season_name = seasons[2] # Лето
    else:
        season_name = seasons[3] # Осень
    print(f"Месяц: {month_name}")
    print(f"Время года: {season_name}")
else:
    print("Ошибка: введено недопустимое число ")

# Нахождение дискриминанта и корней квадратного уравнения
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
if a == 0 and b == 0 and c == 0:
    print("Корень - любое число")
elif a == 0 and b == 0 and c == 1:
    print("Уравнение не имеет корней")
elif a == 0:
    x = c/b
    print("Корень уравнения: ", x)
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = ((-1) * b + math.sqrt(d)) / (2 * a)
        x2 = ((-1) * b - math.sqrt(d)) / (2 * a)
        print("Дискриминант: ", d, "Корни уравнения: ", x1, x2)
    elif d == 0:
        x = ((-1) * b) / (2 * a)
        print("Корень уравнения: ", x)
    else:
        print("Уравнение не имеет корней")
