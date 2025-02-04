from abc import  abstractmethod



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

class MOTO(TRANSPORT):
    def __init__(self, name, speed, tipe):
        super().__init__(name, speed)
        self.tipe = tipe

    def show_trans(self):
        return f"name {self.name}, speed {self.speed}, tipe {self.tipe}"

    def set_speed(self):
        tmp_s = int(input("New speed:"))
        self.speed = tmp_s

obj = CAR("def","def")
obj1 = MOTO("def","def","def")

print(obj.show_trans())
print(obj1.show_trans())

obj.set_speed()
obj1.set_speed()

print(obj.show_trans())
print(obj1.show_trans())