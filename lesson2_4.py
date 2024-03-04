'''Простой класс, представляющий рациональную дробь (num – числитель, den – знаменатель). 
Класс содержит конструктор и методы умножения и деления (дроби на дробь и дроби на целое число). 
Метод создания случайной дроби из заданного диапазона целых чисел объявлен как статический. 
Следует отметить, что в языке имеется готовый тип Fraction в модуле fractions. 
И данный пример нужно рассматривать только как образец для создания собственных классов.'''

class Fraction:

    def __init__(self, num, den):
        if den  == 0:
            raise ValueError("Недопустимое значение атрибута")
        else:
            self.num = num
            self.den = den
    
    @staticmethod
    def check_den(den):
        if den == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

    def __setattr__(self, name, value):
        if name == 'den':
            self.check_den(value)  
        super().__setattr__(name, value)
    
    def multiply(self, other):
       if isinstance(other, Fraction):
           num = self.num * other.num
           den = self.den * other.den
       elif isinstance(other, int):
            if other == 0:
                raise ValueError("Делитель не может быть равен нулю")
            else:
                num = self.num * other
                den = self.den
       else:
           raise TypeError("Invalid type for multiplication")
       return Fraction(num, den)
    
    def division(self, other):
        if isinstance(other, Fraction):
            num = self.num * other.den
            den = self.den * other.num
        elif  isinstance(other, int):
            num = self.num
            den = self.den * other
        else:
            raise TypeError("Invalid type for division")
        return Fraction(num, den)
        
fractions = Fraction(1, 2)
fractions_2 = Fraction(3, 4)

m_result = fractions.multiply(fractions_2)
d_result = fractions.division(fractions_2)
print(m_result.num, '/', m_result.den)
print(d_result.num, '/', d_result.den)

Fraction.check_den(0)
        
  





















