#Вывод алфавита
result = []
for a in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    result.append("|" + a.upper() + a + "|")
print(20*'-')
for i in range(0, len(result), 5):
    print(''.join(result[i:i+5]), "\n" + "-"*20)


#Задача 2 с собаками
m,n = int(input("Введите количество символов по горизонтали: ")), int(input("Введите количество символов по вертикали: "))
print("@") if m == 1 or n == 1 else print("Error") if m <= 0 or n <= 0 else print("@" * m + "\n" + ("@" + " " * (m - 2) + "@\n") * (n - 2) + "@" * m)


#1. Вычислить и вывести на экран сумму кубов натуральных чисел от 1 до n включительно...
n = int(input("Введите предел: "))
if n <= 100:
    a = sum([a**3 for a in range(1, n+1)])
    print("Предел: ",a)
else:
    print("Error")


#2. Выведите на экран таблицу умножения чисел от одного до девяти.
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')  
    print()




