# Polymorphism
# Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(),
# які виводять в консоль відповідно, для методу wheels() - 4 та 8, а для методу mode_of_transport() -
# "Private usage", "Public usage". Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом for
# по списку та викликати методи на кожному елементу списку.
class Car:
    def wheels(self):
        print("Number of wheels: 4")

    def mode_of_transport(self):
        print("Mode of transport: Private usage")


class Bus:
    def wheels(self):
        print("Number of wheels: 8")

    def mode_of_transport(self):
        print("Mode of transport: Public usage")


mazda = Car()
alpha_romeo = Car()
sprinter = Bus()
marshrutka = Bus()

traffic = [mazda, alpha_romeo, sprinter, marshrutka]

for transport in traffic:
    transport.wheels()
    transport.mode_of_transport()

print('*' * 40)


# Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію.
# Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.

class Vehicle:
    def desc(self):
        print("This is a vehicle")

    def wheels(self):
        print("It has some wheels")


class Car(Vehicle):
    def desc(self):
        print("This is a car.")

    def wheels(self):
        print("It has 4 wheels")


class Bus(Vehicle):
    def desc(self):
        print("This is a bus.")

    def wheels(self):
        print("It has 8 wheels")


generic_vehicle = Vehicle()
car1 = Car()
bus1 = Bus()

generic_vehicle.desc()
generic_vehicle.wheels()

car1.desc()
car1.wheels()

bus1.desc()
bus1.wheels()
