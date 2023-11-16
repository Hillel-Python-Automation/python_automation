# Polymorphism
# 1)

class Car:
    def wheels(self):
        print("4")

    def mode_of_transport(self):
        print("Private usage")


class Bus:
    def wheels(self):
        print("8")

    def mode_of_transport(self):
        print("Public usage")


car = Car()
bus = Bus()

spisok = [car, bus]
for i in spisok:
    i.wheels()
    i.mode_of_transport()


# 2)
class Vehicle:
    def desc(self):
        print("Transport")

    def wheels(self):
        print("Kolichestvo koles")


class Car(Vehicle):
    def desc(self):
        print("Audi")

    def wheels(self):
        print("4 kolesa")


class Bus(Vehicle):
    def desc(self):
        print("Gasel")

    def wheels(self):
        print("6 koles")


car = Car()
bus = Bus()

car.desc()
car.wheels()
bus.desc()
bus.wheels()

# Encapsulation

class Clasniy_class:
    def __init__(self, _a, __a):
        self._a = _a
        self.__a = __a

new = Clasniy_class(1, 2)
print(new._a)
print(new.__a)