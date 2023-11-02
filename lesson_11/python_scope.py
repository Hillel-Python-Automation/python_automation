x = 10  # глобальна змінна


def func():
    x = 5
    print('local', x)
    x = 15
    print('local', x)


def func2():
    global x
    print('global before change', x)
    x = 25
    print('global after change', x)


def func3():
    x = 7

    def func_nested():
        nonlocal x
        print(f"nonlocal", x)
        x = 8

    func_nested()
    print('local', x)


func()
func2()
func3()
# func_nested()
print(f"global var:", x)

