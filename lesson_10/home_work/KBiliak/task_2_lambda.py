# Написати лямбда функцію яка приймає 2 числа як аргументи та повертає більше з
# них (використовуйте тернарний if)

def return_bigger_num(x, y):
    return x if x > y else y

rn = return_bigger_num(77, 6)
print(rn)

result = lambda x, y: x if x > y else y
if __name__ == "__main__":
    print(result(x=6, y=9))