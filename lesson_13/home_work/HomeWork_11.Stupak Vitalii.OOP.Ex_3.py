class MyClass:
    def __init__(self):
        self._a = 10
        self.__a = 20

my_object_1 = MyClass()

print('Accessing _a: ', my_object_1._a)
print('Accessing __a: ', my_object_1.__a)

