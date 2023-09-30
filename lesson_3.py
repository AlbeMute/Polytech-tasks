# 1
'''
a = float(input("Введите цену за 1 кг: "))
for kg in range(1, 11):
    b = kg * a
    print(f"Стоимость {kg} кг конфет: {b} рублей")


#2
x = 1
a = []
while x != 0:
    x = int(input("Введите число: "))
    a.append(x)
s = sum(a)
b = len(a)
print("Сумма чисел: ", s, "Кол-во чисел: ", b)


#3
list = [1, '2', 3, 4, '5']
e = []
for i in list:
    i = int(i)
    e.append(i)
s = sum(e)
print(s)


result = [f"{lit.upper()}{lit}" for lit in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"]
print(20 * "-")
for i in range(0, len(result), 5):
    _ = [print("|", "||".join(result[i:i+5]), "|" + "\n" + "-" * 20)]

'''
result = []
for a in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    result.append("|" + a.upper() + a + "|")
print(20*'-')
for i in range(0, len(result), 5):
    print(''.join(result[i:i+5]), "\n" + "-"*20)
