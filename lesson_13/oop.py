import math
# Encapsulation


class MyClass:
    def __init__(self, public, protected, private):
        self.public = public
        self._protected = protected
        self.__private = private

    def get_private(self):
        return self.__get_private()

    def __get_private(self):
        return f"This is the private variable with the value {self.__private}"

    @property
    def protected(self):
        return self._protected

    @protected.setter
    def protected(self, value):
        self._protected = value


# Polymorphism
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return NotImplemented


if __name__ == "__main__":
    myclass = MyClass(3, 2, 1)

    print(myclass.public)
    myclass.public = 7
    print(myclass.public)

    print(myclass.protected)
    myclass.protected = 8
    print(myclass.protected)

    print(myclass.get_private())
    myclass.protected_ = 4
    print(myclass.protected_)
    print(myclass.__dir__())
    del myclass.protected_
    print(myclass.__dir__())

    circle = Circle(14)
    print(circle.area())

    triangle = Triangle(4, 5, 6)
    print(triangle.area())
