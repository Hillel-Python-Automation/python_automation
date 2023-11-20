from classmethod_and_staticmethod import Person, People


class NewPerson(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class NewPeople(People):
    def __init__(self, name, age):
        super().__init__(name, age)


if __name__ == "__main__":
    var1 = NewPerson('New', 1)
    print(var1)
    print(var1.get_person_details())
    print(var1.is_iam_adult())
    print(var1.is_adult(34))
    print(Person.is_adult(34))
    print(var1.get_counter())
    print("_"*30)
    var2 = NewPeople('NewPeople', 2)
    print(var2)
    print(var2.name, var2.age)
    print(var2.create_instance_from_year_of_birth('NewPeople2', 2000).name)
    print(NewPeople.create_instance_from_year_of_birth('NewPeople3', 2005).name)

