'''
#1
import re 

def check_car_number(number):
    patt = r'^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'
    if re.match(patt, number):
        return "Частный легковой автомобиль"
    else:
        return "Некорректный номер"
    
def check_taxi_number(number):
    patt = r'^[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}$'
    if re.match(patt, number):
        return "Такси"
    else:
        return "Некорректный номер"
    
print(check_car_number("А123ВС77792"))
print(check_car_number("М456ОР11"))

print(check_taxi_number("ОВ7653У981"))
print(check_taxi_number("КМ321444"))

#2
import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

text = 'Hello world! bro, -razvivaisya-'
print(count_words(text))
'''

#import re

#with open('task_2.txt', 'r') as file:
 #   text = file.read()
  #  word_count = len(re.findall(r'\b\w+\b', text))

#print(word_count)

import re

print(len(re.findall(r'\b\w+\b', open(r'/home/albemute/Polytech-tasks/task_2.txt').read())))



























