from abc import ABC, abstractmethod


# Abstract class minimal requirements. It should be inherited from ABC class and has at least one abstractmethod
# Abstract class are not allowed to have class instances
class AbstractClass(ABC):
    @abstractmethod  # This method should be implemented in every class inherited from this class
    def method(self):
        pass

    def method2(self): # This method might be implemented might be not.
        print("I'm method2")


class AbstractClassWithoutAbstractMethod(ABC):
    def method(self):
        print("Hello, I'm method from AbstractClassWithoutAbstractMethod class")


class ClassWithAbstractMethod:
    @abstractmethod
    def abstract_method(self):
        pass


class InheritedFrom(AbstractClass):
    # pass
    def method(self):
        print("hello from InheritedFrom class")


class InheritedFromClass(AbstractClassWithoutAbstractMethod):
    pass


class InheritedFromClassWithAbsMethod(ClassWithAbstractMethod):
    def abstract_method(self):
        print('hello')


# Example

class Polygon(ABC):

    @abstractmethod
    def number_of_sides(self):
        pass


class Triangle(Polygon):
    def number_of_sides(self):
        print("I have 3 sides")


class Hexagon(Polygon):
    pass
    # def number_of_sides(self):
    #     raise NotImplementedError


class Pentagon(Polygon):

    def number_of_sides(self):
        print("I have 5 sides")


if __name__ == "__main__":
    inherited = InheritedFrom()
    print(type(inherited))
    inherited.method()
    inherited.method2()
    without_abstract_method = InheritedFromClass()
    print(type(without_abstract_method))
    print(isinstance(without_abstract_method, AbstractClassWithoutAbstractMethod))
    print(isinstance(without_abstract_method, ABC))
    without_abstract_method.method()
    abstract_method_class = ClassWithAbstractMethod()
    print(abstract_method_class)
    print(type(abstract_method_class))
    abstract_method_class.abstract_method()
    print(abstract_method_class.abstract_method())
    abstract_method_class_inherited = InheritedFromClassWithAbsMethod()
    abstract_method_class_inherited.abstract_method()
    print(abstract_method_class_inherited.abstract_method())
    triangle = Triangle()
    triangle.number_of_sides()
    pentagon = Pentagon()
    pentagon.number_of_sides()
    hexagon = Hexagon()


