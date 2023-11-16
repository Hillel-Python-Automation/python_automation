class Car:

    def wheels(self):
        return 4

    def _mode_of_transport(self):
        return 8


class Bus:
    def wheels(self):
        return 4

    def mode_of_transport(self):
        return 8


car = Car()
bus = Bus()
alist = [car, bus]

# for a in alist:
    # print(a.wheels())
    # print(a._mode_of_transport())
    # print(a.mode_of_transport())


class Vehicle:
    def desk(self):
        return 1

    def wheels(self):
        return 4

class Plane(Vehicle):
    def desk(self):
        return 2

    def wheels(self):
        return 2


class Ship(Vehicle):
    def desk(self):
        return 2

    def wheels(self):
        return 0
