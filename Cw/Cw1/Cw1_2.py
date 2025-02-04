# import os
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

class TRANSPORT:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    @abstractmethod
    def show_trans(self):
        pass

    @abstractmethod
    def set_speed(self):
        pass


class CAR(TRANSPORT):
    def __init__(self, name, speed):
        super().__init__(name, speed)
    def show_trans(self):
        return f"name {self.name}, speed {self.speed}"
    def set_speed(self):
        tmp_s = int(input("New speed:"))
        self.speed = tmp_s