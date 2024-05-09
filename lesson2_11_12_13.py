class LocationManager:
    def assign_location(self, employee, country):
        employee.set_location(country)

class Person:
    __slots__ = ('name', 'phone', 'location', '__salary')
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.__salary = 0  
        self.location = None

    # def __setattr__(self, key, value):
    #     if key == 'salary':
    #         raise AttributeError("Direct modification of salary is not allowed. Use set_salary method.")
    #     super().__setattr__(key, value)

    # def __getattr__(self, item):
    #     if item == 'salary':
    #         return self.__salary  # Return the private attribute
    #     raise AttributeError(f"'{type(self).__name__}' object has no attribute '{item}'")
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)) or new_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = new_salary 



    # def set_salary(self, new_salary):
    #     if not isinstance(new_salary, (int, float)) or new_salary < 0:
    #         raise ValueError("Salary can not be negative.")
    #     self.__salary = new_salary  # Set the private attribute

    def get_salary(self):
        return self.__salary
    
    def set_location(self, new_location):
        self.location = new_location

    def get_location(self):
        return self.location
    
    # def update_salary(self, new_salary):
    #     self.set_salary(new_salary)

    def update_salary(self, new_salary):
        self.__salary = new_salary

class Persons_ID:
    ID = 0
    
    def __init__(self):
        Persons_ID.ID += 1
        self.id = Persons_ID.ID

    def save_sell_log(self, salary):
        print(f"{self.id}: received salary - {salary}")

class Manager(Person, Persons_ID):
    __slots__ = ()
    def __init__(self, name, phone):
        Person.__init__(self, name, phone)
        Persons_ID.__init__(self)
    
    def assign_location(self, country):
        self.set_location(f'Manager office in {country}')

    def go_on_vacation(self):
        print(f"Manager {self.name} is going on vacation in December!")

    def update_salary(self, new_salary):
        return super().update_salary(new_salary)
    
class Developer(Person, Persons_ID):
    __slots__ = ()
    def __init__(self, name, phone):
        Person.__init__(self, name, phone)
        Persons_ID.__init__(self)

    def update_salary(self, new_salary):
        super().update_salary(int(new_salary * 1.2))

    def assign_location(self, country):
        self.set_location(f'Development center in {country}')
    
    def go_on_vacation(self):
        print(f"Developer {self.name} is going on vacation in July!")

m = Manager("Bob", "654321")
d = Developer("Charlie", "987654")
m.update_salary(1000)
d.update_salary(1000)
m.assign_location('Russia')
d.assign_location('France')
m.uwu = 2


m.save_sell_log(m.get_salary())
d.save_sell_log(d.get_salary())

print(m.location)
print(d.location)
# print(m.go_on_vacation())  
# print(d.go_on_vacation())

print(f"Manager ID: {m.id}, Developer ID: {d.id}")

employees = [Manager("Bob", '123'), Developer("Alice", '234'), Manager("Charlie", '345'), Developer("David", '456')]
for employee in employees:
    employee.go_on_vacation()


















# from accessify import private, protected


# class Person:
#     def __init__(self, name, phone, salary=0):
#         self.name = name
#         self.phone = phone
#         self.__salary = salary
#         self.set_salary(0)

#     def set_salary(self, new_salary):
#         if not isinstance(new_salary, (int, float)) or new_salary < 0:
#             raise ValueError("Зарплата не может быть отрицательной.")
#         self.__salary = new_salary  

#     def make_new_salary(self, new_salary):
#         self.set_salary(new_salary) 

#     def get_salary(self):
#         return self.__salary

# class Manager(Person):
#     def __init__(self, name, phone):
#         super().__init__(name, phone)

#     def update_salary(self, new_salary):
#         super().make_new_salary(new_salary)

# class Developer(Person):
#     def __init__(self, name, phone):
#         super().__init__(name, phone)

#     def update_salary(self, new_salary):
#         super().make_new_salary(int(new_salary * 1.2))

# class MixinLog:
#     ID = 0
#     def __init__(self):
#         self.ID += 1
#         self.id = self.ID
    

# m = Manager("Bob", "654321")
# d = Developer("Charlie", "987654")
# m.update_salary(1000)
# d.update_salary(1000)

# m.__salary = 1000
# d.__salary = 100

# print(m.get_salary())  
# print(d.get_salary())  
# print()





