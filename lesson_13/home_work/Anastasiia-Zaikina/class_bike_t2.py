from class_vehicle_t2 import Vehicle


class Bike(Vehicle):
    def __init__(self, color, model, speeds):
        super().__init__(color, model)
        self.speeds = speeds

    def desc(self):
        super().desc()
        print(self.speeds)

    def wheels(self):
        print(2)
