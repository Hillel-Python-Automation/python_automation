"""Створити два класи Car та Bus, обидва мають мати 2 методи wheels() та mode_of_transport(),
які виводять в консоль відповідно, для методу wheels() - 4 та 8, а для методу mode_of_transport() - "Private usage", "Public usage".
Створити об'єкти цих класів, покласти їх у список а потім пройшовшись циклом for по списку та викликати методи на кожному елементу списку."""

from class_car_t1 import Car
from class_bus_t1 import Bus

car = Car()
bus = Bus()

vehicle = [car, bus]

for element in vehicle:
    element.wheels()
    element.mode_of_transport()
