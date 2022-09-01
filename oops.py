'''Object oriented Programming Languages'''

#Object
class RailwayForm:
    '''Class and Object'''
    formType :"RailwayForm"
    def print_Data(self):
        print(f"Name is {self.name}")
        print(f"Name is {self.train}")

aashiApplication = RailwayForm()
aashiApplication.name = "Aashi"
aashiApplication.train = "Shatabdi"
aashiApplication.printData()

class Student:
    def __init__(self):
        self.is_registered = False

    def register(self):
        self.is_registered = True
