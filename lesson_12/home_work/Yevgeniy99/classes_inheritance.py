#1. Створити простий, пустий клас без реалізації - BaseClass
class SimpleClass:
    pass

#2. Створити клас який успадковується від класу з пункта 1.
# Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.
class SupremeClass(SimpleClass):
    def __init__(self, new_param):
        self.new_param = new_param

    def new_method(self):
        print(self.new_param)
#3. Створити клас з методом return_fields() який нічого не повертає (... | pass)

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def return_fields(self):
        pass

#4.Створити клас, який прийматиме 2 параметри, успадкований від класу з пункту 3
class MySubClass(MyClass):
    # Визначаємо конструктор класу
    def __init__(self, name, age, hobby, skill):
        super().__init__(name, age)
        self.hobby = hobby
        self.skill = skill

    def return_fields(self):
        # Метод виводить поля класу
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Hobby: {self.hobby}")
        print(f"Skill: {self.skill}")
#Створити клас, який прийматиме 3 параметри, успадкований від класу з пункту 3
# і перевизначити метод return_fields() який виведе поля класу.
# Створюємо клас з ім'ям MyOtherSubClass, який успадковує від класу MyClass
class MyOtherSubClass(MyClass):
    # Визначаємо конструктор класу
    def __init__(self, name, age, country, city, job):
        super().__init__(name, age)
        self.country = country
        self.city = city
        self.job = job
    def return_fields(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Job: {self.job}")


