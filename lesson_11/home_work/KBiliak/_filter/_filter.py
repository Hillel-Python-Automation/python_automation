# 1. Використовуючи функцію filter() вивести тільки парні числа зі списку.
alist = [1, 2, 2, 3, 4, 5, 6, 6, 7, 6.7]


result = filter(lambda a: (a % 2 == 0), alist)
even_nums = list(result)
print(even_nums)

# 2. Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.

words = ["lambda", "code", "criteria", "python"]


result_1 = list(filter(lambda a_word: "a" in a_word, words))
print(result_1)



