class People:
    'Какой-то класс'
    age = 16
    hair = 'brown'
    religion = 'christianity'
    
    def set_height(self, height):
        self.height = height
    
    def set_eyes_color(self, eyes_color):
        self.set_eyes_color = eyes_color

martin = People()
martin.set_height(175)
martin.set_eyes_color('red')
print(martin.height)
print(martin.set_eyes_color)

print(martin.__dict__)
