from abc import abstractmethod

# 1. Створити клас з абстрактним методом. Створити об'єкт даного класу.
class ABC:
    pass

# 2. Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.
class ABCMeta(ABC):
    pass

# 3. Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від абстрактного класу і створіть
# об'єкт нового класу.
class ABC2():
    @abstractmethod  # This method should be implemented in every class inherited from this class
    def method(self):
        pass


class NewABC2(ABC2):
    pass


if __name__ == "__main__":
    name = ABCMeta()
    name2 = NewABC2()

# 4. Створити конструкції try-except для арифметичної операції, роботи з колекціями.
    a = [1,2,3,4,5]
    b = [6,7,8,9,"ten"]
    try:
        print(a+b)
    #    print(a+"b")
    except TypeError:
        raise BaseException("Type Error")

# 5. Створити конструкції try-except-else
    try:
        print(a+b)
    except ValueError:
        raise BaseException("Value Error")
    else:
        print("Happy weekend!")

# 6. Створити конструкції try-except-else-finally
    try:
        print(a+b)
    except ValueError:
        raise BaseException("Value Error")
    else:
        print("Happy weekend!")
    finally:
        print("Finally I finish!")

# 7. Створити конструкції try-except-finally
    try:
        print(a+b)
    except ValueError:
        raise BaseException("Value Error")
    finally:
        print("Finally I finish!")

# Створити конструкції try-except з більше ніж трьома except`ами
    try:
        print(a+b)
    except ValueError:
        raise BaseException("Value Error")
    except TypeError:
        raise BaseException("Type Error")
    except ZeroDivisionError:
        raise BaseException("Divide by zero")
    except SyntaxError:
        raise BaseException("Some Syntax error")
