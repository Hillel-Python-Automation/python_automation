class Person:
    counter: int = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def get_person(self):
        return f"name - {self.name}, age - {self.age}"

    def __del__(self):
        del self
        Person.counter -= 1

    @staticmethod
    def get_counter():
        return Person.counter





if __name__ == "__main__":
    person1 = Person("Kate", 25)
    print(person1.get_person())
    print(person1.counter)
    print(person1.get_counter())

    person2 = Person("Kate", 26)
    print(person2.get_person())
    print(person2.counter)
    print(person2.get_counter())