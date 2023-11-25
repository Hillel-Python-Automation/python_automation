##Створити простий, пустий клас без реалізації - BaseClass##
print(70*'*')
print('Ex.- 1')

class Students:
    pass
print(Students)

##Створити клас який успадковується від класу з пункта 1.
#Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.##
print(70*'*')
print('Ex.- 2')
class New_students(Students):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def Dear(self):
        print("Dear"" students let me introduce our new student", self.firstname, self.lastname, "his", self.age, "years old")
a = New_students("Robert", "Rodriges", "25")
a.Dear()

##Створити клас з методом return_fields() який нічого не повертає (... | pass) #
print(70*'*')
print('Ex.- 3')

class New():
    def return_fields(self):
        return 'Empty fields'
a = New()
results = a.return_fields()
print(results)


##Створити клас, який прийматиме 2 параметри,
#успадкований від класу з пункту 3 і перевизначити метод return_fields() який виведе поля класу.
print(70*'*')
print('Ex.- 4')


class New1(New):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def return_fields(self):
        return f"{self.brand}, {self.model}"

a = New1("brand", "model")
print(a.return_fields())


##Створити клас, який прийматиме 3 параметри,
# успадкований від класу з пункту 3 і перевизначити метод return_fields() який виведе поля класу.##
print(70*'*')
print('Ex.- 5')

class New2(New):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def return_fields(self):
        return f"{self.brand}, {self.model}, {self.year}"
s = New2("brand", "model","year")
print(s.return_fields())