'''Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, 
а с помощью метода to_pounds() они переводятся в фунты. 
Чтобы закрыть доступ к переменной kg она реализовала методы set_kg() - для задания нового значения килограммов, get_kg() 
- для вывода текущего значения кг. 
Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений. 
Помогите ей переделать класс с использованием функции property() и свойств-декораторов.'''

from typing import Any


class  KgToPounds():
    def __init__(self, kg):
        self.__kg = kg
    
    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, value):
        if value < 0:
            raise ValueError('Вес не может быть отрицательным')
        self.__kg = value


    def to_pounds(self):
        return (self.__kg * 2.2)
    
    def __setattr__(self, name, value):
        if name == 'note' or name == '_KgToPounds__kg':
            super().__setattr__(name, value)
        else:
           raise AttributeError('Нельзя вводить другие атрибуты')

    def __add__(self, other):
        if isinstance(other, int):
            return KgToPounds(self.__kg + other)
        else:
            raise  TypeError
          

c = KgToPounds(10)
print(c.kg)
print(c.to_pounds())

b = c + 1
print(b.kg)
# c.note = 'ks'
# x = c.note
# print(x)
# c.old = 30




# try:
#     carrot = KgToPounds(-10)
# except ValueError as e:
#     print(e)

















