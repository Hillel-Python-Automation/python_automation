from abc import ABC, abstractmethod


# 1)
class New_Class:
    @abstractmethod
    def abstract_method(self):
        pass


new_object = New_Class()


# 2)
class Some_Class(ABC):
    pass


some_object = Some_Class()


# 3)
class New_abstract_Class(ABC):
    @abstractmethod
    def new_abstract_method(self):
        pass


class Some_new_Class(New_abstract_Class):
    pass


new_some_object = Some_new_Class()

# 4)
try:
    a = int(input("vvedite pervoe chislo: "))
    b = int(input("vvedite vtoroe chislo: "))
    print(a / b)
except ZeroDivisionError as s:
    print("Na nol' delit nelzya ((")


try:
    a = ["hello", "world", "!"]
    b = int(input("vvedite index: "))
    print(a[b])
except IndexError as s:
    print(f"Indexa pod nomerom {b} nety v spiske {a}")



# 5)
try:
    a = int(input("vvedite pervoe chislo: "))
    b = int(input("vvedite vtoroe chislo: "))
    print(a / b)
except ZeroDivisionError as s:
    print("Na nol' delit nelzya ((")
else:
    print("Shalost udalas")



# 6)
try:
    a = int(input("vvedite pervoe chislo: "))
    b = int(input("vvedite vtoroe chislo: "))
    print(a / b)
except ZeroDivisionError as s:
    print("Na nol' delit nelzya ((")
else:
    print("Shalost udalas")
finally:
    print(f"Mi seychas delili chislo {a} na chislo {b}")



# 7)
try:
    a = int(input("vvedite pervoe chislo: "))
    b = int(input("vvedite vtoroe chislo: "))
    print(a / b)
except ZeroDivisionError as s:
    print("Na nol' delit nelzya ((")
finally:
    print(f"Mi seychas delili chislo {a} na chislo {b}")



# 8)
try:
    a = int(input("vvedite pervoe chislo: "))
    b = int(input("vvedite vtoroe chislo: "))
    c = int(a / b)
    d = ["hello", "world", "!"]
    print(d[c])
except ZeroDivisionError as s:
    print("Na nol' delit nelzya ((")
except ValueError as s:
    print("Vi vveli ne chislo")
except IndexError as s:
    print(f"Indexa pod nomerom {c} nety v spiske {d}")



