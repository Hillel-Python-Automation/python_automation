from abc import ABC, abstractmethod

# Створити клас з абстрактним методом. Створити об'єкт даного класу.
class AbstrClass():
    @abstractmethod
    def method(self):
        pass
    
abstrclss = AbstrClass()

# Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.
class AbstrctInher(ABC):
    def method(self):
        print('Abstract Class Inherited from ABC')

abstrInhABC = AbstrctInher()

# Створити абстрактний клас з абстрактним методом.
class AbstrClsFrmABC(ABC):
    @abstractmethod
    def method(self):
        pass

# Створити новий клас успадкований від абстрактного класу і створіть об'єкт нового класу.
class AbstrClsInherFrmAbstrct(AbstrClsFrmABC):
    def method(self):
        print('Abstract class inherited from abstract class with abstract method')

absclsfromabstrcmeth = AbstrClsInherFrmAbstrct()

#Cтворити конструкції try-except для арифметичної операції, роботи з колекціями.
try:
    print(66/2)
except Exception as ex:
    print('You are trying to divide by zero, that is not allowed')
print('o'*45)     
#Створити конструкції try-except-else

try:
    c = int(input('Enter first value: '))
    v = int(input('Enter second value: '))
    res=c/v
except ZeroDivisionError as zde:
    print(zde)
else:
    print(res)    
         
print('o'*45)     
#Створити конструкції try-except-else-finally
try:
    q = input("Input first value: ")
    w = input("Input second value: ")
    result = int(q)/int(w)
except (ValueError, ZeroDivisionError):
    print("Something went wrong...")
else:
    print("Let's make it square: ", result**2)
finally:
    print("This is the end")

print('o'*45)    
#Створити конструкції try-except-finally
try:
    value1 = int(input('First value: '))    
    value2 = int(input('Second value: '))
    multiply = value1 * value2
except ValueError as ve:
    print("try again now with numbers")
finally:
    print("Let's hope this will work")          
    
    
print('o'*45) 
#Створити конструкції try-except з більше ніж трьома except`ами
try:
    a = int(input('Enter first value: '))
    b = int(input('Enter second value: '))
    print(a/b)
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print(ve)
except Exception as ex:
    print('Please fix all issues') 