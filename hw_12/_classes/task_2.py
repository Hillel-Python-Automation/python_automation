# 2. Створити клас який успадкований від класу ABC або metaclass=ABCMeta і
# створити його об'єкт.
from abc import ABC

class InheritedFromABC(ABC):
    def method(self):
        print("Hello, python")

fromabc = InheritedFromABC()
