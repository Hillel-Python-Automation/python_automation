##1. Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(),
# які виводять в консоль відповідно, для методу wheels() - 4 та 8,
# а для методу mode_of_transport() - "Private usage", "Public usage".
# Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом for по списку
# та викликати методи на кожному елементу списку.##
print(70*'*')
print('Ex. 1')

class Car:
    def wheels(self):
        print('Number of wheels: 4')

    def mode_of_transport(self):
        print('Private usage')

class Bus:
    def wheels(self):
        print('Number of wheels: 8')

    def mode_of_transport(self):
        print('Public usage')

New_Car = Car()
New_Bus = Bus()

transport = [New_Car, New_Bus]

for transport in transport:
    transport.wheels()
    transport.mode_of_transport()
print()

##2.Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію.
# Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.##
print(70*'*')
print('Ex. 2')

class Vehicle():
    def desc(self):
        print('Private type of vehicle for private traveling')

    def wheels(self):
        print('This vehicle have 4 wheels')

class Of_road_vehicle(Vehicle):
    def desc(self):
        print('Private type of vehicle for of-road traveling')
    def wheels(self):
        print('This vehicle have 4 wheels for of-road traveling')

class Road_vehicle(Vehicle):
    def desc(self):
        print('Private type of vehicle for longer traveling')
    def wheels(self):
        print('This vehicle have 4 wheels too for longer traveling')

New_vehicle = Vehicle()
New_of_road_vehicle = Of_road_vehicle()
New_road_vehicle = Road_vehicle()

New_vehicle.desc()
New_vehicle.wheels()
print()

New_of_road_vehicle.desc()
New_of_road_vehicle.wheels()
print()

New_road_vehicle.desc()
New_road_vehicle.wheels()
print()


### Encapsulation#Створити клас з 2 змінними (_a and __a),
# Створити об'єкт класу та показати доступ до цих змінних. (Очікувано отримаємо помилку при доступі до __а)
print(70*'*')
print('Ex. 1(Encapsulation)')

class New_class():
    def __init__(self):
        self._a = 'Name'
        self.__a = 'Surname'

    def print_class(self):
        print('Access _a:', self._a)
        print('Access __a:', self.__a)

new_object = New_class()

new_object.print_class()

print('Access to _a:', new_object._a)
print('Access to __a:', new_object.__a)