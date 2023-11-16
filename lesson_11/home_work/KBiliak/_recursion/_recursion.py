# Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# 1, 2, 3, 4, 5, 6, 7, 8, 9
n = 10


def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibo = fib(n - 1)
        fibo.append(fibo[-1] + fibo[-2])
        return fibo


result = fib(n)
print(result)

# Написати функцію яка виводить ряд Фібоначчі використовуючи рекурсію
# 0, 1, 1, 2, 3, 5, 8, 13, 21
# 1, 2, 3, 4, 5, 6, 7, 8, 9

a_list = [0, 1]


def fibo(a_list, n):
    while len(a_list) < n:
        if len(a_list) == 2:
            add_sum = sum(a_list)
            a_list.append(add_sum)
        else:
            last = a_list[-1] + a_list[-2]
            a_list.append(last)

    return a_list


f = fibo(a_list, 20)
print(f)
