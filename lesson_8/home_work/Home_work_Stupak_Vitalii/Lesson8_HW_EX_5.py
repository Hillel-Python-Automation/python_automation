def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Результат : {result}')
        return result
    return wrapper
@print_result
def add(a,b):
    return a + b

@print_result
def multiply(x,y):
    return x * y

res_1 = add(10, 100)
res_2 = multiply(55, 50)

