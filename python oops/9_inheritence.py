#Inheritence

"""
Single Inheritence

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car):
    def __init__(self,name):
        self.name = name

car1 = Toyota("fortuner")
car2 = Toyota("prius")
print(car1.name)
car1.start()
print(car1.color)
"""


"""Multi-Level Inheritence


class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car):
    def __init__(self,brand):
        self.brand = brand
class fortuner(Toyota):
    def __init__(self,type):
        self.type = type

c1 = fortuner("diesel")
c1.start()
"""



"""Multiple Inheritence


class A:
    var_a = "welcome to class A"
class B:
    var_b = "welcome to class B"

    
class C(A,B):
    var_c = "welcome to class C"

c1 = C()
print(c1.var_c+"\n"+c1.var_b+"\n"+c1.var_a)
"""

""" super() method
class Car:

    def __init__(self,type):
        self.type = type

    
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = Toyota("prius","EV")
print(car1.type)
"""













