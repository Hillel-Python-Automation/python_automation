from classmethod_and_staticmethod import Person


class NewPerson(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


if __name__ == "__main__":
    var1 = NewPerson("name", 22)
    print(var1)
    print(var1.get_person())
    print(var1.count_year_of_birth(2000))