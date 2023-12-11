from class_vehicle_t2 import Vehicle


class Truck(Vehicle):
    def __init__(self, color, model, lifting_capacity):
        super().__init__(color, model)
        self.lifting_capacity = lifting_capacity

    def desc(self):
        super().desc()
        print(self.lifting_capacity)

    def wheels(self):
        print(10)
       