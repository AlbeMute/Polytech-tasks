'''
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears
only once in the original string,or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.
'''
def duplicate(word):
    word = word.lower()
    return "".join([")" if word.count(char) > 1 else "(" for char in word])

print(duplicate("din"))  #Output: (((
print(duplicate("recede"))  #Output: ()()()
print(duplicate("Success"))  #Output: )())())
print(duplicate("(( @"))  #Output: ))(((

word = input("Введите слово: ")

print("После преобразований получается: ", duplicate(word))