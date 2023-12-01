# Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of
# _transport(), які виводять в консоль відповідно, для методу wheels() - 4 та
# 8, а для методу mode_of_transport() - "Private usage", "Public usage".
# Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом
# for по списку та викликати методи на кожному елементу списку.

class Car:

    def wheels(self):
        print(4)

    def _mode_of_transport(self):
        print(8)


class Bus:
    def wheels(self):
        print(4)

    def mode_of_transport(self):
        print(8)


car = Car()
# car.wheels(4)
# car._mode_of_transport(8)
#
bus = Bus()
# bus.wheels(4)
# bus.mode_of_transport(8)

list_1 = [car.wheels(), car._mode_of_transport(), bus.wheels(), bus.mode_of_transport()]

for a in list_1:
    print(a)

