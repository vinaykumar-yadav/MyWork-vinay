class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def myFunc(self):
        print("Hello my name is :" + self.name)

objPerson = Person('vinay', 28)
objPerson.myFunc() 
