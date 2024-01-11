#1. Створити два класи Car та Bus, обидва мають мати 2 методи
# wheels() та mode_of_transport(), які виводять в консоль відповідно, для методу wheels() - 4 та 8,
# а для методу mode_of_transport() - "Private usage", "Public usage".
# Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом for по списку
# та викликати методи на кожному елементу списку.

class Car:
    def wheels(self):
        print(4)

    def mode_of_transport(self):
        print("Private usage")

class Bus:
    def wheels(self):
        print(8)

    def mode_of_transport(self):
        print("Public usage")
car1 = Car()
bus1 = Bus()

vehicles = [car1, bus1]

for vehicle in vehicles:
    vehicle.wheels()
    vehicle.mode_of_transport()
#Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію.
# Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.

class Vehicle:
    def desc(self):
        print("It is a vehicle")

    def wheels(self):
        print("The vehicle has wheels")

class Bike(Vehicle):
    def desc(self):
        print("It is a bike")

    def wheels(self):
        print("The bike has 2 wheels")

class Truck(Vehicle):
    def desc(self):
        print("It is a truck")

    def wheels(self):
        print("The truck has 6 wheels")


# Encapsulation
class MyClass:
    def __init__(self, a, b):
        self._a = a
        self.__a = b
obj = MyClass(10, 20)

print(obj._a)
print(obj.__a)


