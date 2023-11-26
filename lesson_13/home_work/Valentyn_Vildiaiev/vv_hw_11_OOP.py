# Polymorphism

# Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(),
# які виводять в консоль відповідно, для методу wheels() - 4 та 8, а для методу mode_of_transport()
# - "Private usage", "Public usage". Створити об'єкти цих класів,
# покласти їх у список а потім пройшовшись циклом for по списку та викликати методи на кожному елементу списку.
class Car:
    def __init__(self):
        self.wheels = 4
        self.mode_of_transport = "Private usage"

    def wheels_info(self):
        print(self.wheels)

    def mode_of_transport_info(self):
        print(self.mode_of_transport)


class Bus:
    def __init__(self):
        self.wheels = 8
        self.mode_of_transport = "Public usage"

    def wheels_info(self):
        print(self.wheels)

    def mode_of_transport_info(self):
        print(self.mode_of_transport)


car = Car()
bus = Bus()

vehicles = [car, bus]

for vehicle in vehicles:
    vehicle.wheels_info()
    vehicle.mode_of_transport_info()


# Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію.
# Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.

class Vehicle:
    def desc(self):
        print("This is a vehicle")

    def wheels(self):
        print("It has 4 wheels")


class Vehicle1(Vehicle):
    def desc(self):
        print("This is a new vehicle")

    def wheels(self):
        print("It has 4 wheels")


class Vehicle2(Vehicle):
    def wheels(self):
        print("This one has 6 wheels")

    def desc(self):
        print("It's a track")


# Encapsulation

# Створити клас з 2 змінними (_a and __a), Створити об'єкт класу та показати доступ до цих змінних.
# (Очікувано отримаємо помилку при доступі до __а)

class TwoVars():
    def __init__(self):
        self._a = "Access to _a is granted"
        self.__a = "Access to private var is forbidden"

    @property
    def access(self):
        return self._a

    # @property
    # def accessSec(self):
    # return self.__a


var = TwoVars()
print(var.access)
print(var.__a)
