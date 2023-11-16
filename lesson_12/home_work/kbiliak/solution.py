import datetime


# 1. Створити простий, пустий клас без реалізації - BaseClass
class BaseClass:
    ...


# 2. Створити клас який успадковується від класу з пункта 1. Додати для
# ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.
class InheritedFromBaseClass(BaseClass):
    def __init__(self, name):
        self.name = f"Hello, {name}"

    def print_name(self):
        return self.name


# 3. Створити клас з методом return_fields() який нічого не повертає (... | pass)
class ClassWhichReturnsNothing:
    def return_fields(self):
        ...


# 4. Створити клас, який прийматиме 2 параметри, успадкований від класу з
# пункту 3 і перевизначити метод return_fields() який виведе поля класу.
class ReturnFieldsFromCWRN(ClassWhichReturnsNothing):
    def __init__(self, age, occupation):
        self.age = age
        self.occupation = occupation

    def return_fields(self):
        return f"Age: {self.age}\nOccupation: {self.occupation}"

# 5. Створити клас, який прийматиме 3 параметри, успадкований від класу з
# пункту 3 і перевизначити метод return_fields() який виведе поля класу.
class ClassWith3Param(ClassWhichReturnsNothing):
    def __init__(self, birthday, specialization, level):
        self.birthday = birthday
        self.specialization = specialization
        self.level = level

    def return_fields(self):

        if self.specialization.lower() in ["manual", "automatization"]:
            return f"birtday: {self.birthday},\nspecialization: " \
                   f"{self.specialization},\nlevel: {self.level}"
        else:
            return "choose manual or automatization option "


base_class = BaseClass
return_name = InheritedFromBaseClass("Kate")
return_age_occupation = ReturnFieldsFromCWRN(19, "QA")
return_birth_spec_level = ClassWith3Param\
    (datetime.date(1997, 10, 8), "manual", "senior")

if __name__ == "__main__":
    print(return_name.print_name())
    print(return_age_occupation.return_fields())
    print(return_birth_spec_level.return_fields())
