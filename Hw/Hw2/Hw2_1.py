import os
from abc import  abstractmethod


class Bank:
    def __init__(self, name, street, count_of_cash):
        self.name = name
        self.street = street
        self.count_of_cash = count_of_cash

    @abstractmethod
    def set_count_of_cash(self):
        new_cash = int(input("New cash: "))
        self.count_of_cash = new_cash


class Terminal(Bank):
    def __init__(self, name, street, count_of_cash):
        super().__init__(name, street, count_of_cash)
        self.name = name
        self.street = street
        self.count_of_cash = count_of_cash

    def set_count_of_cash(self):
        new_cash = int(input("New cash: "))
        self.count_of_cash = new_cash

    def show(self):
        file = "Terminal.txt"
        with open("Terminal.txt", "w") as terminalFile:
            terminalFile.write(f"Name: {self.name}")
            terminalFile.write(f"street: {self.street}")
            terminalFile.write(f"count of cash: {self.count_of_cash}")
        with open(file, "r") as terFile:
            print(terFile.readlines())


class Postmat(Bank):
    def __init__(self, name, street, count_of_cash):
        super().__init__(name, street, count_of_cash)
        self.name = name
        self.street = street
        self.count_of_cash = count_of_cash

    def set_count_of_cash(self):
        new_cash = int(input("New cash: "))
        self.count_of_cash = new_cash

    def show(self):
        file = "Postmat.txt"
        with open("Postmat.txt", "w") as postmatFile:
            postmatFile.write(f"Name: {self.name}, street: {self.street}, count of cash: {self.count_of_cash}")
        with open(file, "r") as posFile:
            print(posFile.readlines())

obj = Terminal("def","def",1)
obj1 = Postmat("def","def",1)

obj.set_count_of_cash()
obj1.set_count_of_cash()

obj.show()
obj1.show()

