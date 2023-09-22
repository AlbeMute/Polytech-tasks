#1
numbers = [1, 2, 3, 4, 5]
if numbers:
    print(sum(numbers)/len(numbers))
else:
    print(0)
#numbers = [1, 2, 3, 4, 5]
#print(sum(numbers)/len(numbers)) if numbers else print(0)

#2
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
numbers = []

if 1 <= a <= 3 and 1 <= b <= 3 and 1 <= c <= 3:
 numbers.append([a, b, c])
print(numbers)
