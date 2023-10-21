
#1
'''
Дан двумерный массив размером 3x3. 
Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива. Вывести полученные значения.
'''
from random import randint

n = 3
arr = list()

for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(randint(1, 9))
  arr.append(brr)

for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()

max_column = max(arr[i][2] for i in range(3))
max_row = max(arr[1])

print("Максимальное значение в третьем столбце:", max_column)
print("Максимальное значение во второй строке:", max_row)

#2
'''
Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. 
Вывести оба массива.
'''
from random import randint

n = randint(1, 8)
m = randint(1, 8) 
arr = []

for i in range(n):
  brr = []
  for j in range(m):
    brr.append(randint(-8, 8))
  arr.append(brr)

for i in range(n):
  for j in range(m):
    print(arr[i][j], end=' ')
  print()

new_arr = [[0] * m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if arr[i][j] > 0:
      new_arr[i][j] = 1

print("Новая матрица:")
for i in range(m):
  for j in range(n):
    print(new_arr[j][i], end=' ')
  print()

#3
'''
Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, 
т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
'''
from random import randint

n = 3
arr = [[2, 7, 6],
       [9, 5, 1],
       [4, 3, 8]]

magic_sum = sum(arr[0])

for row in arr:
    if sum(row) != magic_sum:
        print("Матрица не является магическим квадратом.")
        exit()

for j in range(n):
    column_sum = sum(arr[i][j] for i in range(n))
    if column_sum != magic_sum:
        print("Матрица не является магическим квадратом.")
        exit()

print("Матрица является магическим квадратом.")

#4
'''
Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
'''
from random import randint

n = 3
arr = list()

for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(randint(1, 9))
  arr.append(brr)

for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()

def symmetric(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return False
    
    return True

print("1 Матрица симметричная: ", symmetric(arr)) 

#symmetric arr
arr = [[1, 2, 3], 
      [2, 4, 5], 
      [3, 5, 6]]

print("2 Матрица симметричная: ", symmetric(arr))

#5
'''
Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов.
Вывести на печать найденные строки и суммы их элементов.
'''
from random import randint

n = randint(3, 6)
m = randint(3, 6) 
arr = []

for i in range(n):
  brr = []
  for j in range(m):
    brr.append(randint(1, 8))
  arr.append(brr)

for i in range(n):
  for j in range(m):
    print(arr[i][j], end=' ')
  print()

max_sum = sum(arr[0])
max_sum_row = arr[0]
min_sum = sum(arr[0])
min_sum_row = arr[0]

for row in arr[1:]:
    row_sum = sum(row)
    if row_sum > max_sum:
        max_sum = row_sum
        max_sum_row = row
    elif row_sum < min_sum:
        min_sum = row_sum
        min_sum_row = row

print("Строка с наибольшей суммой элементов: ", max_sum_row)
print("Сумма элементов строки с наибольшей суммой: ", max_sum)
print("Строка с наименьшей суммой элементов: ", min_sum_row)
print("Сумма элементов строки с наименьшей суммой: ", min_sum)

#6
'''
Дана действительная матрица размером n х m, все элементы которой различны. 
В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем, нечетное - единицей. 
Вывести на экран новую матрицу.
'''
from random import randint

n = randint(3, 6)
m = randint(3 , 6) 
arr = []

for i in range(n):
  brr = []
  for j in range(m):
    brr.append(randint(2, 8))
  arr.append(brr)

print("Исходная матрица: ")
for i in range(n):
  for j in range(m):
    print(arr[i][j], end=' ')
  print()

new_arr = []

for i in range(n):
    row = arr[i]
    min_element = min(row)
    new_row = []
    for j in range(m):
        if row[j] == min_element:
            if row[j] % 2 == 0:
                new_row.append(0)
            else:
                new_row.append(1)
        else:
            new_row.append(row[j])
    new_arr.append(new_row)
print()

print("\nОбновленная матрица: ")
for i in range(n):
    for j in range(m):
        print(new_arr[i][j], end=' ')
    print()







