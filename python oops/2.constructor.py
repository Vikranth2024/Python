# class Student:
#     def __init__(self):
#         print(self)
#         print("Constructor is called")
# s1 = Student()

class Student:
    def __init__(self,fullname):
        self.name = fullname
s1 = Student("Sam Konstas")
print(s1.name) 