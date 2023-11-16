class Alphbabet:
    def __init__(self, _a, __a):
        self._a = 1
        self.__a = 2

    def _return_a(self, _a):
        return _a


    def __return_a(self, __a):
        return __a

alphabet = Alphbabet(1, 2)

print(alphabet._return_a(1))
print(alphabet.__return_a(2))