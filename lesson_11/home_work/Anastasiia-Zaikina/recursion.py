# Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію
def recurs_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recurs_fibonacci(n - 1) + recurs_fibonacci(n - 2)
