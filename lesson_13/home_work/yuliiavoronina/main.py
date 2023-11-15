# Polymorphism

#1. Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(), які
# виводять в консоль відповідно, для методу wheels() - 4 та 8, а для методу mode_of_transport() -
# "Private usage", "Public usage". Створити об'єкти цих класів, покласти їх у список а потім пройшовшись
# циклом for по списку та викликати методи на кожному елементу списку.

class Car:
    def wheels(self):
        return "Car has 4 weels."

    def mode_of_transport(self):
        return "Private usage"


class Bus:
    def wheels(self):
        return "Bus has 8 weels."

    def mode_of_transport(self):
        return "Public usage"




#2. Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію.
# Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.


class Vehicle:
    def desc(self):
        print("Test desc.")

    def wheels(self):
        print("Some number of weels.")


class Rocket(Vehicle):
    def desc(self):
        print("Identified fly object.")

    def wheels(self):
        print("No wheels")


class UFO(Vehicle):
    def desc(self):
        print("Unidentified fly object.")

    def wheels(self):
        print("We don't know.")


# Encapsulation

#3. Створити клас з 2 змінними (_a and __a), Створити об'єкт класу та показати доступ до цих змінних.
# (Очікувано отримаємо помилку при доступі до __а)

class Task:
    def __init__(self, num1, num2, num3):
        self.public = num1
        self._protected = num2
        self.__private = num3

    def get_private(self):
        return self.__get_private()

    def __get_private(self):
        return "The private variable is " + str(self.__private)

    @property
    def protected(self):
        return self._protected

    @protected.setter
    def protected(self, value):
        self._protected = value


if __name__ == "__main__":
    lst = [Car(), Bus()]

    for i in lst:
        print(i.wheels(), i.mode_of_transport())

    myclass = Task(55, 66, 77)

    print(myclass.public)
    print(myclass.protected)
    print(myclass.get_private())
