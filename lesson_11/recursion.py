def factorial(x):
    if x == 1:
        # print(x)
        return 1
    else:
        # print(x)
        return x * factorial(x - 1)


num = 50
print("The factorial of", num, "is", factorial(num))
