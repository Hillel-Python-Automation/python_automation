import datetime


# 1. Створити простий, пустий клас без реалізації - BaseClass
class BaseClass:
    ...


# 2. Створити клас який успадковується від класу з пункта 1. Додади для
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
print(return_name.print_name())

return_age_occupation = ReturnFieldsFromCWRN(19, "QA")
print(return_age_occupation.return_fields())

return_birth_spec_level = ClassWith3Param\
    (datetime.date(1997, 10, 8), "manual", "senior")
print(return_birth_spec_level.return_fields())
