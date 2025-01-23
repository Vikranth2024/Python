class Person:
    __name = "Viki"

    def __hello(self):
        print("Hello guys!")

    def welcome(self):
        self.__hello()
        print(self.__name)
    
p1 = Person()
p1.welcome()
