#1(1,2,3)
def read_last(lines, file):
    if lines <= 0:
        print("Количество строк должно быть положительным числом")
        return

    try:
        with open(file, 'r') as f:
            lines_list = f.readlines()
            if lines > len(lines_list):
                lines = len(lines_list)
            for line in lines_list[-lines:]:
                print(line.strip())
    except FileNotFoundError:
        print("Файл не найден")
read_last(3, 'article.txt')



import os

def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

# Пример использования
print_docs('path/to/your/directory')





def longest_words(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        words = []
        max_length = 0
        for line in lines:
            line = line.strip()
            line_words = line.split()
            for word in line_words:
                word_length = len(word)
                if word_length > max_length:
                    words = [word]
                    max_length = word_length
                elif word_length == max_length:
                    words.append(word)
    return words

# Пример использования на файле "article.txt"
result = longest_words("article.txt")
print(result)



#2(4)
def text_editor():
    file_name = input("Введите имя файла: ")
    file_name += ".txt"

    lines = []
    while True:
        line = input("Введите строку текста (или введите пустую строку для сохранения файла): ")
        if not line:
            break
        lines.append(line)

    with open(file_name, 'w') as file:
        file.write('\n'.join(lines))

    print(f"Файл '{file_name}' успешно сохранен.")

# Запуск программы
text_editor()



#3(5)
import csv
import time

def create_csv():
    with open('rows_300.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['№', 'Секунда', 'Микросекунда'])
        
        for i in range(1, 301):
            seconds = time.strftime('%S')
            microseconds = round(time.clock_gettime(time.CLOCK_MONOTONIC) * 1000)

            writer.writerow([i, seconds, microseconds])
            time.sleep(0.01)
    
    print("CSV-файл успешно создан.")

# Запуск программы
create_csv()

#4(6)
from random import randint
import os
from PIL import Image, ImageDraw

def circles_generator(num_of_circles=100):
    # Создание директории "circles" (если она не существует)
    if not os.path.exists("circles"):
        os.makedirs("circles")

    for i in range(num_of_circles):
        # Создание изображения с белым фоном
        img = Image.new("RGB", (600, 600), "white")
        
        # Создание экземпляра объекта ImageDraw
        draw = ImageDraw.Draw(img)
        
        # Генерация случайных цветов
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = (r, g, b)
        
        # Расчет координат и рисование круга
        center = (300, 300)
        radius = 300
        draw.ellipse((center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius), fill=color)
        
        # Сохранение изображения в формате jpg
        file_name = f"circles/circle{i+1}.jpg"
        img.save(file_name, "JPEG")

# Запуск программы
circles_generator()

