#task1
def check_integer(num):
 try:
  int(num)
  return True
 except ValueError:
  return False

a = input("Введите первое целое число: ")
b = input("Введите второе целое число: ")
c = input("Введите третье целое число: ")

if check_integer(a) and check_integer(b) and check_integer(c):
 a = int(a)
 b = int(b)
 c = int(c)

 if a < b:
  if a < c:
   y = a
  else:
   y = c
 else:
  if b < c:
   y = b
  else:
   y = c
 print("Минимальное число:", y)
else:
 print("Ошибка, введите целые числа!")

 #task2
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))
numbers_in_interval = []
if 1 <= a <= 3:
 numbers_in_interval.append(a)

if 1 <= b <= 3:
 numbers_in_interval.append(b)

if 1 <= c <= 3:
 numbers_in_interval.append(c)
print("Числа, принадлежащие интервалу [1,3]: ", numbers_in_interval)