class Car:
    def wheels(self):
        print('Wheels: 4')
    def mode_of_transport(self):
        print('mode_of_transport : Private usage')

class Bus:
    def wheels(self):
        print('Wheels : 8')
    def mode_of_transport(self):
        print('mode_of_transport : Public usage')

car_instance = Car()
bus_instance = Bus()

vehicles = [car_instance, bus_instance]

for vehicle in vehicles:
    vehicle.wheels()
    vehicle.mode_of_transport()
    print()

