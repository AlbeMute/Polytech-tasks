def duplicate(word):
    word = word.lower()
    return "".join([")" if word.count(char) > 1 else "(" for char in word])

print(duplicate("din"))  #Output: (((
print(duplicate("recede"))  #Output: ()()()
print(duplicate("Success"))  #Output: )())())
print(duplicate("(( @"))  #Output: ))(((

word = input("Введите слово: ")

print("После преобразований получается: ", duplicate(word))