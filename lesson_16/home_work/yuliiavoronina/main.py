from yuliia_voronina import Wheel

small_wheel = Wheel(diameter=15, material='Aluminum')
small_wheel.display_info()

large_wheel = Wheel.create_large_wheel()
large_wheel.display_info()

diameter_valid = Wheel.validate_diameter(18)
print(f"Diameter is valid: {diameter_valid}")
