class Vehicle:
    def __init__(self, wheels, gear, fuel):
        self.wheels = wheels
        self.gear = gear
        self.fuel = fuel

    def get_wheels(self):
        return self.wheels

    def get_fuel(self):
        return self.fuel

    def get_gear(self):
        return self.gear

    def refill(self, fuel):
        if self.fuel.lower() != fuel.lower():
            return f"You need to use {self.fuel} instead of {fuel}"
        return "The fuel tank is refilled"

    def get_description(self):
        return f"The vehicle has {self.wheels} wheels and {self.gear} gear and uses {self.fuel}"

    def __eq__(self, other):
        return self.wheels == other.wheels and self.gear == other.gear and self.fuel == other.fuel


class Body:
    def __init__(self, body_type, doors, steering_wheel):
        self.body_type = body_type
        self.doors = doors
        self.steering_wheel = steering_wheel

    def get_description(self):
        return f"The body has body type: {self.body_type} with {self.doors} doors and {self.steering_wheel} steering wheel"


class Tesla(Vehicle):
    def __init__(self, wheels, gear, fuel, model, battery_capacity):
        super().__init__(wheels, gear, fuel)
        self.model = model
        self.battery_capacity = battery_capacity

    def refill(self, fuel):
        if self.fuel.lower() != fuel.lower():
            return f"Hey! It's Tesla! Use the charger!"
        return "The battery is charged"

    def drive(self):
        return "To the 100 km/p for less then 3s"

    def get_model(self):
        return f"The model of this Tesla is {self.model}"


class Ford(Vehicle):
    def __init__(self, wheels, gear, fuel):
        Vehicle.__init__(self, wheels, gear, fuel)


class MultiInheritance(Body, Vehicle):
    def __init__(self, wheels, gear, fuel, body_type, doors, steering_wheel):
        Vehicle.__init__(self, wheels, gear, fuel)
        Body.__init__(self, body_type, doors, steering_wheel)
        self.fuel = 'Water'

    def get_doors(self):
        return f"Number of doors {self.doors}"

    def get_description(self):
        return Vehicle.get_description(self) + ". " + Body.get_description(self)

    def __str__(self):
        return Vehicle.get_description(self) + ". " + Body.get_description(self)

    def __repr__(self):
        return f"MultiInheritance(wheels={self.wheels}, gear='{self.gear}', fuel='{self.fuel}')"


if __name__ == "__main__":
    var_vehicle = Vehicle(4, "Manual", "Diesel")
    var_vehicle2 = Vehicle(4, "Manual", "Diesel")

    print(var_vehicle.__eq__(var_vehicle2))
    print(var_vehicle)
    print(var_vehicle.fuel)
    print(var_vehicle.wheels)
    var_vehicle.gear = 'Automatic'
    print(var_vehicle.gear)
    print(var_vehicle.get_gear())
    print(var_vehicle.get_fuel())
    print(var_vehicle.get_wheels())
    print(var_vehicle.refill("Gas"))
    print(var_vehicle.refill("Diesel"))

    var_tesla = Tesla(wheels=4, gear="Automatic", fuel='Electric energy', model="Y", battery_capacity='200kWh')
    print(var_tesla)
    print(var_tesla.fuel)
    print(var_tesla.wheels)
    print(var_tesla.gear)
    print(var_tesla.get_gear())
    print(var_tesla.get_fuel())
    print(var_tesla.get_wheels())
    print(var_tesla.refill("Gas"))
    print(var_tesla.refill("Diesel"))
    print(var_tesla.refill("Electric energy"))
    print(var_tesla.drive())
    print(var_tesla.get_model())

    print(type(var_vehicle))
    print(type(var_tesla))
    print(isinstance(var_tesla, Tesla))
    print(isinstance(var_vehicle, Vehicle))
    print(isinstance(var_tesla, Vehicle))
    var_ford = Ford(3, "Manual", "Petrol")
    print(var_ford)
    print(var_ford.wheels)

    multi_inheritance = MultiInheritance(4, "Manual", 'Gas', 'hatchback', 3, 'left')
    print(multi_inheritance)
    print(multi_inheritance.fuel)
    print(multi_inheritance.wheels)
    print(multi_inheritance.gear)
    print(multi_inheritance.doors)
    print(multi_inheritance.get_doors())
    print(multi_inheritance.body_type)
    print(multi_inheritance.steering_wheel)

    print(multi_inheritance.get_description())

    # MRO -> Method Resolution Order

    print(MultiInheritance.mro())

    print(isinstance(multi_inheritance, MultiInheritance))
    print(isinstance(multi_inheritance, Vehicle))
    print(isinstance(multi_inheritance, Body))
    print(isinstance(multi_inheritance, object))

    print(multi_inheritance.__str__())
    print(multi_inheritance.__repr__())
    print(str(multi_inheritance))
    print(dir(multi_inheritance))
    print(repr(multi_inheritance))


