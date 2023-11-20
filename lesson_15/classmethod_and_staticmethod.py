import datetime as dt


# Staticmethod
# Не приймає посилання на об'єкт класу.
# Можна викликати на самому класі не створюючи його об'єкт.
# Не має доступу до інформації про стан класу (об'єкту)
class Person:
    __counter: int = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__counter += 1

    def get_person_details(self):
        return f"The person's name is {self.name} and he/she is {self.age} years old"

    def __del__(self):
        del self
        Person.__counter -= 1

    @staticmethod
    def get_counter():
        return Person.__counter

    @staticmethod
    def is_adult(age):
        return age >= 18

    def is_iam_adult(self):
        return self.age >= 18

    @staticmethod
    def count_year_of_birth_by_age(age):
        return dt.date.today().year - age


class Utils:
    @staticmethod
    def is_palindrome(string):
        return string == string[::-1]

    @staticmethod
    def is_float(number):
        return str(number).count('.') == 1


# Classmethod
# Приймає посилання на клас
# Має доступ до інформації про клас, його структуру, та як створити об'єкт класу
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_instance_from_year_of_birth(cls, name, year):
        return cls(name, dt.date.today().year - year)


if __name__ == "__main__":
    person1 = Person('Kate', 25)
    print(person1.get_person_details())
    # print(Person.counter)
    print(Person.get_counter())
    person2 = Person("Peter", 30)
    print(person2.get_person_details())
    # print(Person.counter)
    print(Person.get_counter())

    print(Person.count_year_of_birth_by_age(25))
    print(person2.count_year_of_birth_by_age(30))

    del person1
    print(Person.get_counter())
    print(Person.get_person_details(person2))
    print('_' * 30)
    people1 = People('Miki', 35)
    people2 = People.create_instance_from_year_of_birth('Naomi', 1999)

    print(people1.name, people1.age)
    print(people2.name, people2.age)
    print('_' * 30)
    print(Utils.is_palindrome('121'))
    print(Utils.is_palindrome('топот'))
    print(Utils.is_palindrome('abba'))
    print(Utils.is_palindrome('mom'))
    print('_'*30)
    print(Person.is_adult(person2.age))
    print(person2.is_iam_adult())
    print('_' * 30)
    print(Utils.is_float(4.5))
    print(Utils.is_float(45))
