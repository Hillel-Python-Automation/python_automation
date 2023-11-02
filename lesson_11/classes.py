# Empty class
class Class:
    ...


var_class = Class()

print(Class)
print(var_class)


class Car:
    def __init__(self, model, year, fuel_type, gear):
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.__gear = gear

    def set_gear(self, gear):
        if gear.lower() in ['automatic', 'manual']:
            self.__gear = gear

    def get_gear(self):
        return self.__gear

    def get_str(self):
        return f"Car model {self.model} produced in {self.year} uses fuel {self.fuel_type} and has {self.__gear} gear!"


toyota = Car('COROLLA', 2015, 'Petrol', 'Automatic')
honda = Car('CIVIC', 2010, 'Petrol', 'Automatic')

class_list = [toyota, honda]
# toyota2 = Car()
print(toyota)
print(toyota.year)
print(toyota.model)
print(toyota.get_gear())
print(toyota.fuel_type)

# toyota.__gear = "Manual"
toyota.set_gear('Manual')

print(honda)
print(honda.year)
print(honda.model)
print(honda.fuel_type)

for car in class_list:
    print(car)
    print(car.year)
    print(car.model)
    print(car.fuel_type)
    print(car.get_gear())
    print(car.get_str())
