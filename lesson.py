import math

#task 1
a = input("Ваши фамилия, имя? ")
b = input("Сколько Вам лет?" )
c = input("Где вы живете?" )
print("Ваши фамилия, имя", a)
print("Ваш возраст", b)
print("Вы живете в", c)

#task 2
x = int(input())
t = int(input())
z = round((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t)))*math.pow(math.e, x), 2)
print(z)