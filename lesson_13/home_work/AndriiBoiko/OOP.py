# Polymorphism
class Car:
    def wheels(self):
        return 4

    def mode_of_transport(self):
        return "Private usage"


class Bus:
    def wheels(self):
        return 8

    def mode_of_transport(self):
        return "Public usage"


car = Car()
bus = Bus()

vehicles = [car, bus]

for vehicle in vehicles:
    print(vehicle.wheels())
    print(vehicle.mode_of_transport())


class Vehicle:
    def desc(self):
        return "This is a vehicle"

    def wheels(self):
        return 4


class Car(Vehicle):
    def desc(self):
        return "This is a car"

    def wheels(self):
        return 4


class Bus(Vehicle):
    def desc(self):
        return "This is a bus"

    def wheels(self):
        return 6


car = Car()
bus = Bus()

print(car.desc())
print(car.wheels())

print(bus.desc())
print(bus.wheels())

# Encapsulation

class EncapExample:
    def __init__(self):
        self._a = 1
        self.__a = 2


obj = EncapExample()

print(obj._a)
print(obj.__a)