
class Student:
    def __init__(self,name, age,registration):
        self.name = name
        self.age = age
        self.registration = registration
        
    def display_information(self):
        print(f'Name: {self.name} Age: {self.age} Registration: {self.registration}')
        
        
class Teacher:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id