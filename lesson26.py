class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Name:", self.name)


class Student(Person):
    def study(self):
        print(self.name, "is studying Python")


s = Student("Rani love")

s.introduce()
s.study()
