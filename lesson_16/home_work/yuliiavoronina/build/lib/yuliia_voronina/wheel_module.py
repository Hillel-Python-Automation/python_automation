class Wheel:
    def __init__(self, diameter, material):
        self.diameter = diameter
        self.material = material

    def display_info(self):
        print(f"Wheel: Diameter - {self.diameter}, Material - {self.material}")

    @classmethod
    def create_large_wheel(cls):
        return cls(diameter=20, material='Steel')

    @staticmethod
    def validate_diameter(diameter):
        return diameter > 0
