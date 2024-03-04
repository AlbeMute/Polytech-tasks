#1
'''
class Sauce:
    'вкус соуса'

    def __init__(self, taste, addition = ''):
        self.taste = taste
        self.addition = addition
        
    def show_my_souce(self):
        if self.addition:
            print(f'Соус {self.taste} c добавкой {self.addition}')
        else:
            print('Майонез')

sauce = Sauce('сырный')
sauce.show_my_souce()

sauce.addition = 'сметана'
sauce.show_my_souce()
'''

'''#2
class Employee:

    def __init__(self, name, age, salary, bonus = ''):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus

    def get_name(self):
        print(f'имя сотрудника {self.__name}')
    def get_age(self):
        print(f'возраст сотрудника {self.__age}')
    def get_salary(self):
        print(f'зарплата сотрудника {self.__salary}')
    def set_bonus(self, bonus):
        self.__bonus = bonus
    def get_bonus(self):
        print(f'бонус сотрудника {self.__bonus}')
    def get_total_salary(self):
        print(f'общая зарплата {self.__bonus+self.__salary}')

employee = Employee('Valera', 30, 30000)
employee.get_name()
employee.get_age()
employee.get_salary()
employee.set_bonus(5000)
employee.get_total_salary()'''

#3
'''class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def is_triangle(self):
        if not all(map(self.is_positive, self.sides)):
            return 'С отрицательными числами ничего не выйдет!'
        if not self.is_valid_triangle():
            return 'Жаль, но из этого треугольник не сделать.'
        return 'Ура, можно построить треугольник!'

    def is_positive(self, num):
        return num > 0

    def is_valid_triangle(self):
        sides = sorted(self.sides)
        return sides[0] + sides[1] > sides[2]'''

'''class TriangleChecker:

    @classmethod
    def is_triangle(cls, a, b, c):
        if not all(map(cls.is_positive, (a, b, c))):
            return 'С отрицательными числами ничего не выйдет!'
        if not all(map(cls.is_number, (a, b, c))):
            return 'Нужно вводить только числа!'
        if not sum((a, b, c))/2 > max((a, b, c)):
            return 'Жаль, но из этого треугольник не сделать.'
        return 'Ура, можно построить треугольник!'

    @staticmethod
    def is_positive(num):
        return num > 0

    @staticmethod
    def is_number(num):
        return isinstance(num, (int, float))
    
print(TriangleChecker.is_triangle(2, 3, 4))
print(TriangleChecker.is_triangle(77, 3, 4))
print(TriangleChecker.is_triangle(2, -3, 4))
print(TriangleChecker.is_triangle(2, 3, 'Сторона_3'))'''





    
























