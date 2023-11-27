class Vehicle :
    def desc(self):
        print('Vehicle ')
    def wheels(self):
        print('Wheels of vehicle')

class Car (Vehicle):
    def desc(self):
        print('Car 1')
    def wheels(self):
        print('Wheels of car')
class Bus (Vehicle):
    def desc(self):
        print('Bus 1')
    def wheels(self):
        print('Wheels of bus')

vehicle_instance = Vehicle()
car_instance = Car()
bus_instance = Bus()

vehicle_instance.desc()
vehicle_instance.wheels()

car_instance.desc()
car_instance.wheels()

bus_instance.desc()
bus_instance.wheels()