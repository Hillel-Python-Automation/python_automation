# Ex1.
class BaseClass:
    pass


# Ex2.
class DerivedClass(BaseClass):
    def __init__(self, base_param, derived_param):
        super().__init__()
        self.base_param = base_param
        self.derived_param = derived_param

    def display_params(self):
        print(f'Base parameter: {self.base_param}, Derived Parameter: {self.derived_param}')


derived_instance = DerivedClass('Base Value', 'Derived Value')
derived_instance.display_params()


# Ex3.

class ClassWithNoReturn:
    def return_fields(self):
        pass


# Ex4.

class ClassWithTwoParams(ClassWithNoReturn):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def return_fields(self):
        print(f'Parameters : {self.param1}, {self.param2}')


# Ex5.

class ClassWithThreeParams(ClassWithNoReturn):
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def return_fields(self):
        print(f'Parameters : {self.param1}, {self.param2}, {self.param3}')


instance_three_params = ClassWithThreeParams('Value1', 'Value2', 'Value3')
instance_three_params.return_fields()
