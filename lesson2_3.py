'''Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.'''

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = self.b = self.c = 0
        self.a = self.validate(a)
        self.b = self.validate(b)
        self.c = self.validate(c)

    @classmethod
    def validate(cls, arg):
        if not isinstance(arg, (int, float)):
            raise ValueError('Нужно вводить только числа!')
        if arg <= 0:
            raise ValueError('С отрицательными числами ничего не выйдет!')
        return arg

    def is_triangle(self):
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            return 'Жаль, но из этого треугольник не сделать.'
        return 'Ура, можно построить треугольник!'

triangle1 = TriangleChecker(3, 4, 5)
print(triangle1.is_triangle())

triangle2 = TriangleChecker(1, 1, 10)
print(triangle2.is_triangle())

# triangle3 = TriangleChecker(3, 4, -5)
# print(triangle3.is_triangle())

# triangle4 = TriangleChecker(3, 4, 'ngklengkne')
# print(triangle4.is_triangle())
















'''class TriangleChecker:
    def __init__(self, a, b, c):
        self._validate(a)
        self._validate(b)
        self._validate(c)
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def validate(cls, arg):
        if not isinstance(arg, (int, float)):
            raise ValueError('Нужно вводить только числа!')
        if arg <= 0:
            raise ValueError('С отрицательными числами ничего не выйдет!')
        return arg

    def is_triangle(self):
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            return 'Жаль, но из этого треугольник не сделать.'
        return 'Ура, можно построить треугольник!'

triangle1 = TriangleChecker(3, 4, 5)
print(triangle1.is_triangle())'''

















