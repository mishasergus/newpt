import os
# file = open("text.txt","w")
# file.write("SUS")
# file.close()
from abc import  abstractmethod

"""file = open("ITSTEP TEST.txt","w")
inf = ''
while inf != "stop":
    inf = input("INFO:").lower()
    file.write(inf)

file.close()"""
"""file = "NEW.txt"


with open("NEW.txt","w") as itstepFile:
    itstepFile.write("INF")

with open(file,"r") as myFile:
    print(myFile.readlines())"""

"""file = "I.txt"

name = input("n: ")
age = int(input("n: "))
birth = int(input("n: "))
id = int(input("n: "))

with open("I.txt","w") as IFile:
    IFile.write(f"name: {name}  ")
    IFile.write(f"age: {age}  ")
    IFile.write(f"birth: {birth}  ")
    IFile.write(f"id: {id}  ")

with open(file,"r") as myFile:
    print(myFile.readlines())"""

file = "Student.txt"


class Person:
    def __init__(self, name, lastname, id):
        self.name = name
        self.lastname = lastname
        self.id = id

    @abstractmethod
    def show_info(self):
        pass



class Student(Person):
    def __init__(self, name, lastname, id):
        super().__init__(name, lastname, id)

    def show_info(self):
        with open("Student.txt", "w") as IFile:
            IFile.write(f"name: {self.name}  ")
            IFile.write(f"lastname: {self.lastname}  ")
            IFile.write(f"id: {self.id}  ")

        with open(file, "r") as myFile:
            print(myFile.readlines())
obg = Person("def", "def", "def")
obg1 = Student("def", "def", "def")
obg1.show_info()