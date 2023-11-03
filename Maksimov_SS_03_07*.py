
#2
'''
Выберите любую папку на своем компьютере, имеющую вложенные директории. 
Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
'''

import os

def print_docs(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            print(os.path.join(root, file))

current_dir = os.getcwd()
print_docs(current_dir)



#3
'''
Документ "..." содержит следующий текст: "....."
Требуется реализовать функцию `longest_words(file)`, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).  
'''
import os

def longest_words(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        
    words = []
    max_l = 0
    
    for line in lines:
        line_word = line.strip().split()
        
        for word in line_word:
            word_l = len(word)
            
            if word_l > max_l:
                words = [word]
                max_l = word_l
            elif word_l == max_l:
                words.append(word)
    
    return words

print(longest_words(input("Введите путь к файлу: ")))

#4
'''
Составьте программу - простейший редактор текстовых файлов.
Алгоритм работы программы:
  1. Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение `.txt`.
  2. Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку.
  3. Если строка пустая или спец. символ - программа сохраняет файл.
'''

def text():
    file_name = input("Введите имя файла: ")
    file_name += '.txt'

    lines = []
    while True:
        line = input("Введите строку текста (или введите пустую строку для сохранения файла): ")
        if not line:
            break
        lines.append(line)

    with open(file_name, 'w') as file:
        file.write('\n'.join(lines))

    print(f"Файл '{file_name}' успешно сохранен.")

text()


























