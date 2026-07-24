class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("----------------")
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Love AK", 23)
s2 = Student("Rahul", 20)
s3 = Student("Anil", 22)

s1.show()
s2.show()
s3.show()
