'''
    Добавить операции сравнения;
    Ввести проверку хэшей: если дроби одинаковые - это один объект экземпляра класса.
'''

from typing import Any
import sympy
class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    @staticmethod
    def check_den(den):
        if den == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

    def __add__ (self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __sub__  (self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __mul__ (self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("Деление на нулевую дробь невозможно")
        return Fraction(self.num * other.den, self.den * other.num)
    
    def __str__(self):
        return str(sympy.Rational(self.num, self.den))
    
    def value(self):
        return round(self.num / self.den, 3)
    
    def __eq__(self, other):
        return sympy.Rational(self.num, self.den) == sympy.Rational(other.num, other.den)

    def __lt__(self, other):
        return sympy.Rational(self.num, self.den) < sympy.Rational(other.num, other.den)

    def __ge__(self, other):
       return sympy.Rational(self.num, self.den) >= sympy.Rational(other.num, other.den)

class New_Fractions:
    def __init__(self, x):
        self.x = x
    
    def __call__(self, fractions, fractions_2):
        return(fractions, )


    # def  new_fraction(self, num, den):
    #     key = (num, den)
    #     if key in self.fractions:
    #         return  self.fractions[key]
    #     else:
    #         frac = Fraction(num, den)
    #         self.fractions[key] = frac
    #         self.hashes[key] =  hash(frac)
    #         return frac
        
    
    # def __hash__(self):
    #     return hash (sympy.Rational(self.num, self.den))
    

fractions = Fraction(1, 2)
fractions_2 = Fraction(1, 2)
# print(f'Дробь_1: {fractions}')
# print(f'Дробь_2: {fractions_2}')

# summation = fractions + fractions_2
# print(f'Сумма дробей: {summation}')

# difference = fractions - fractions_2
# print(f'Разность дробей: {difference}')

# mull = fractions * fractions_2
# print(f'Произведение дробей: {mull}')

# division = (fractions / fractions_2).value()
# print(f'Деление дробей: {division}')

print (f"{fractions} == {fractions_2}: {fractions == fractions_2}")
print  (f"{fractions} < {fractions_2}: {fractions < fractions_2}")
print (f"{fractions} >= {fractions_2}: {fractions >= fractions_2}")

print("один экземпляр класса" if hash(fractions) == hash(fractions_2) else "разных классов")
