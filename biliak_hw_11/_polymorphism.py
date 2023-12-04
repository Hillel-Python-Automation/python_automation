# Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of
# _transport(), які виводять в консоль відповідно, для методу wheels() - 4 та
# 8, а для методу mode_of_transport() - "Private usage", "Public usage".
# Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом
# for по списку та викликати методи на кожному елементу списку.

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


car = Car()
bus = Bus()


list_1 = [car, bus]

for a in list_1:
    a.wheels()
    a.mode_of_transport()


# Створити клас Vehicle який має два методи desc() та wheels() котрі виводять
# в консоль певну інформацію. Створити 2 дочірніх класи успадкованих від класу
# Vehicle та перевизначити зазначені 2 методи.

class Vehicle:
    def desc(self):
        print("vehicle desc")

    def wheels(self):
        print("vehicle wheels")


class Ship(Vehicle):
    def desc(self):
        print("ship desc")

    def wheels(self):
        print("ship wheels")


class Rocket(Vehicle):
    def desc(self):
        print("rocket desc")

    def wheels(self):
        print("rocket desc")


vehicles = [Vehicle(), Ship(), Rocket()]

for vehicle in vehicles:
    vehicle.desc()
    vehicle.wheels()
