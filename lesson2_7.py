'''Написать программу для различных математических действий над обычными дробями.
- Реализовать проверку деления на 0 при инициации объектов.
- Реализовать метод для вычисления точного значения дроби, округлить до 3-его знака после запятой.
- При попытке вывода любой обычной дроби (результат вычислений или объект) сделать красивый вывод.'''
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
    
fractions = Fraction(1, 4)
fractions_2 = Fraction(3, 4)
print(f'Дробь_1: {fractions}')
print(f'Дробь_2: {fractions_2}')

summation = fractions + fractions_2
print(f'Сумма дробей: {summation}')

difference = fractions - fractions_2
print(f'Разность дробей: {difference}')

mull = fractions * fractions_2
print(f'Произведение дробей: {mull}')

division = (fractions / fractions_2).value()
print(f'Деление дробей: {division}')

    

















