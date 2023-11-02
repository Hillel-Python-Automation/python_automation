def func(param): return param * 2


a = func

# lambda

var_lambda = lambda x: x * 2
var_lambda2 = lambda x: x ** 3

var_lamb = lambda x, y: x * y
var_max = lambda x, y: x if x > y else y
var_empty = lambda: print('Hello world')
var_empty2 = lambda x: var_max(var_lambda(x), var_lambda2(x))

if __name__ == '__main__':
    print(a)
    print(a(2))
    print(a('2'))
    print('lambda')
    print(var_lambda)
    print(var_lambda(2))
    print(var_lambda('2'))
    print(var_lambda2)
    print(var_lambda2(2))
    print(var_lambda2(3))
    print('Lambda with 2 parameters')
    print(var_lamb(2, 3))
    var_lamb = None
    print(var_lamb)
    print((lambda x, y: x * y)(3, 4))
    print(var_max(5, 6))
    print(var_max(7, 6))

    var_empty()
    print(var_empty2(3))

    for i in range(0, 11):
        print((lambda x: x * 2 if x % 2 == 0 else x + 1)(i))


# Corner case
    list_of_functions = [lambda x: x + i for i in range(5)]
    print(list_of_functions)
    for function in range(5):
        print(list_of_functions[function](10))
