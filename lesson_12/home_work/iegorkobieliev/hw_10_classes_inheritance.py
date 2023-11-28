print('''
1. Створити простий, пустий клас без реалізації - BaseClass
''')


class BaseClass:
    pass


print(BaseClass())

print('''
2. Створити клас який успадковується від класу з пункта 1. Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.
''')


class InheritedBaseClass(BaseClass):
    def __init__(self, par1):
        super().__init__()
        self.par1 = par1

    def method1(self):
        return self.par1


ibc = InheritedBaseClass(par1=100)
print(ibc)
print(isinstance(ibc, InheritedBaseClass))
print(ibc.method1())

print('''
3. Створити клас з методом return_fields() який нічого не повертає (... | pass) 
''')


class ClassWithMethodThatReturnsNothing:
    def __init__(self):
        pass

    def return_fields(self):
        pass


cwm = ClassWithMethodThatReturnsNothing()
print(cwm)
print(cwm.return_fields())

print('''
4. Створити клас, який прийматиме 2 параметри, успадкований від класу з пункту 3 і перевизначити метод return_fields() який виведе поля класу.
''')


class ClassThatInheritedClass3(ClassWithMethodThatReturnsNothing):
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2

    def return_fields(self):
        return self.par1, self.par2


ic4 = ClassThatInheritedClass3(par1=10, par2=20)
print(ic4)
print(f'(par1, par2) = {ic4.return_fields()}')

print('''
5. Створити клас, який прийматиме 3 параметри, успадкований від класу з пункту 3 і перевизначити метод return_fields() який виведе поля класу.
''')


class Class2ThatInheritedClass3(ClassWithMethodThatReturnsNothing):
    def __init__(self, par1, par2, par3):
        self.par1 = par1
        self.par2 = par2
        self.par3 = par3

    def return_fields(self):
        return self.par1, self.par2, self.par3


ic5 = Class2ThatInheritedClass3(par1=1000, par2=2000, par3=3000)
print(ic5)
print(f'(par1, par2, par3) = {ic5.return_fields()}')
