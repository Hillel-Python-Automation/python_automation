# Дано словник який складається з транспортних засобів та їх маси в кілограмах.
# Складіть список назв транспортних засобів вагою до 5000 кілограмів. У тому
# самому list comprehension зробіть імена ключів великими регістром.
car_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600,
            "Van": 2400, "Semi": 13600, "Bicycle": 7,
            "Motorcycle": 110}



list5 = [name.upper() for name in car_dict.keys() if car_dict[name] < 5000]

print(list5)
