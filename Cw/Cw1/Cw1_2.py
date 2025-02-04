import os
import random
# file = open("text.txt","w")
# file.write("SUS")
# file.close()
from abc import  abstractmethod
from random import randint

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

    @abstractmethod
    def para(self):
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
    def para(self):
        if self.id % 2 != 0:
            self.id = randint(1, 100)
obg = Person("def", "def", "def")
obg1 = Student("def", "def", randint(1, 100))
obg2 = Student("def", "def", randint(1, 100))
obg3 = Student("def", "def", randint(1, 100))
obg4 = Student("def", "def", randint(1, 100))
obg5 = Student("def", "def", randint(1, 100))
obg1.show_info()
ob = [obg1,obg2,obg3,obg4,obg5]
def para_id(ob):
    for i in ob:
        i.para()
        print(i.id)
    for i in ob:
        print(f"End id:{i.id}")

para_id(ob)