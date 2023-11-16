from abc import ABC, abstractmethod


# Interface
# Interface should be inherited from ABC class and have only abstract methods
class IShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass
    