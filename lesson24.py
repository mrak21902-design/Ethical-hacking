class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Love AK", 23)

student1.show()
