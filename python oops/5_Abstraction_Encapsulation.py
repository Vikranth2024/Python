""" Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car has started")
c1 = Car()
c1.start()
"""


#Encapsulation

class Person:
    def __init__(self, name, age):
        self.name = name          # Public information
        self.__age = age          # Private information (double underscore)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age")

# Using the Person class
person = Person("Alice", 30)

# Public information can be accessed directly
print(person.name)  # Output: Alice

# Private information needs special methods
print(person.get_age())  # Output: 30

# Change private information with control
person.set_age(35)
print(person.get_age())  # Output: 35

# Try to set an invalid age
person.set_age(-5)  # Output: Please enter a valid age
