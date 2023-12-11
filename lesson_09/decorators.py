import time


def separator(func):
    def wrapper():
        print()
        print("="*40)
        # print()
        func()
    return wrapper


def calculate_performance(func):
    def wrapper():
        start = time.time()
        print(func())
        print(f"Your function takes {time.time() - start}")

    return wrapper


@separator
@calculate_performance
def function():
    print("I have hust started!")
    time.sleep(3)
    print("I'm finished!")


@separator
@calculate_performance
def function_without_decorator():
    print("I have hust started!")
    time.sleep(3)
    print("I'm finished!")


def make_bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper


@separator
@calculate_performance
@make_bold
def print_text():
    return "Hello, world!"


if __name__ == "__main__":
    function()
    function_without_decorator()
    print_text()
