#1
import re

def check_car_number(number):
    pattern = r'^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'
    if re.match(pattern, number):
        return "Частный легковой автомобиль"
    else:
        return "Некорректный номер"

def check_taxi_number(number):
    pattern = r'^[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}$'
    if re.match(pattern, number):
        return "Такси"
    else:
        return "Некорректный номер"

# Примеры использования
print(check_car_number("А123ВС77792"))  # Частный легковой автомобиль
print(check_car_number("М456ОР11"))  # Частный легковой автомобиль
print(check_car_number("АВ123СТ123"))  # Некорректный номер

print(check_taxi_number("КМ321444"))  # Такси
print(check_taxi_number("ОВ7653У981"))  # Такси
print(check_taxi_number("А234УХ"))  # Некорректный номер

#2
import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

text = "Hello, how are you? I'm doing well, thank you!"
print(count_words(text))  # Вывод: 9

text = "Это пример русского текста."
print(count_words(text))  # Вывод: 3

text = "Word1-Word2-Word3"
print(count_words(text))  # Вывод: 3


word_count = len(open('filename.txt', 'r').read().split())


#3
import re

text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
new_text = re.sub(r'\d{2}:\d{2}(:\d{2})?', '(TBD)', text)

print(new_text)


#4
import re

text = "ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п."
abbreviations = re.findall(r'\b[A-Z]{2,}\b', text)

print(abbreviations)



















