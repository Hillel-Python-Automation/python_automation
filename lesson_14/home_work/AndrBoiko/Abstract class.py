from abc import ABC, abstractmethod

class MyClass(ABC):

    @abstractmethod
    def my_method(self):
        pass

obj = MyClass()

from abc import ABC, abstractmethod

class MyClass(ABC):

    @abstractmethod
    def my_method(self):
        pass

class ChildClass(MyClass):
    def my_method(self):
        print("Hello")

obj = ChildClass()

from abc import ABC, abstractmethod


class AbstractClass(ABC):

    @abstractmethod
    def do_something(self):
        pass


class ConcreteClass(AbstractClass):

    def do_something(self):
        print("Hello")


obj = ConcreteClass()
obj.do_something()

