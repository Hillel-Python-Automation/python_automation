from multipledispatch import dispatch


@dispatch(int, int)
def add(x, y):
    return x + y


@dispatch(object, object)
def add(x, y):
    return "%s + %s" % (x, y)


@dispatch(float, float)
def add(x, y):
    return x + y


if __name__ == "__main__":
    print(add(2, 3))
    print(add(1, 'hello'))
    print(add(1.0, 2.0))
    print(add(1.0, 2))


