print('''
# Polymorphism
1. Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(), які виводять в консоль 
відповідно, для методу wheels() - 4 та 8, а для методу mode_of_transport() - "Private usage", "Public usage". 
Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом for по списку та викликати методи 
на кожному елементу списку.
''')


class Car:
    def wheels(self):
        return 4

    def mode_transport(self):
        return "Private usage"


class Bus:
    def wheels(self):
        return 8

    def mode_transport(self):
        return "Public usage"


vehicle_list = [Car(), Bus()]

for i in vehicle_list:
    print(i)
    print(i.wheels())
    print(i.mode_transport())

print('_' * 30)

print('''
2. Створити клас Vehicle який має два методи desc() та wheels() котрі виводять в консоль певну інформацію. 
Створити 2 дочірніх класи успадкованих від класу Vehicle та перевизначити зазначені 2 методи.
''')


class Vehicle:
    def desc(self):
        pass

    def wheels(self):
        pass


class V1(Vehicle):
    def desc(self):
        return "This is Vehicle V1"

    def wheels(self):
        return 4


class V2(Vehicle):
    def desc(self):
        return "This is Vehicle V2"

    def wheels(self):
        return 3


v_list = [V1(), V2()]
for i in v_list:
    print(i)
    print(i.desc())
    print(i.wheels())

print('_' * 30)
print('''
# Encapsulation
1. Створити клас з 2 змінними (_a and __a), Створити об'єкт класу та показати доступ до цих змінних. 
(Очікувано отримаємо помилку при доступі до __а)
''')


class SomeClass:
    def __init__(self, x, y):
        self._a = x
        self.__a = y


some_class = SomeClass(10, 20)
print(some_class._a)
print(some_class.__a)
