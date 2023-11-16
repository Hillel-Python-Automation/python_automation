#1)
class BaseClass:
    pass

#2)
class NewClass(BaseClass):
    def __init__(self, first_name, second_name):
        super().__init__()
        self.first_name = first_name
        self.second_name = second_name
    def show_first_name(self):
        print(self.first_name)

#3)
class One_more_class:
    def return_fields(self):
        pass

#4)
class Some_class(One_more_class):
    def __init__(self, first_name, second_name):
        super().__init__()
        self.first_name = first_name
        self.second_name = second_name

    def return_fields(self):
        print(self.first_name, self.second_name)

#5)
class Last_class(One_more_class):
    def __init__(self, first_name, second_name, age):
        super().__init__()
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def return_fields(self):
        print(self.first_name, self.second_name, self.age)
