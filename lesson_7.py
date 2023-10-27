import os
#import pillow
#import openpyxl
#os.getcwd()
#os.listdir()   os.walk()

#for adress, names in os.walk(os.getcwd())

#1
n = int(input('Введите количество последних строк, которые нужно вывести: '))

def read_last(lines, file):
    if lines <= 0:
        print('Количество строк должно быть положительным числом')
        return
    
    with open(file, 'r') as f:
        a = f.readlines()
        
    if lines > len(a):
        print('Количество строк превышает количество строк в файле')
        return
    
    last_lines = a[-lines:]
    for line in last_lines:
        print(line.strip())
  
read_last(n, 'article.txt')















