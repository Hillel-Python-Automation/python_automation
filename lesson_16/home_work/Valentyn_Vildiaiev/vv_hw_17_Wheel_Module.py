from python_automation.lesson_13.home_work.Valentyn_Vildiaiev.vv_hw_11_OOP import Car as Cr


class NewClass(Cr):
    def __init__(self):
        super().__init__()

    @classmethod
    def class_meth(cls):
        return f"This will be a class method of {cls.__name__}"

    @staticmethod
    def static_method():
        return "This will be a static method"


lets_call = NewClass()
print('*' * 50)
print(NewClass.class_meth())
print(NewClass.static_method())
dir()
