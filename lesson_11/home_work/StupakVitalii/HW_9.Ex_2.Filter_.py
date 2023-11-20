#Ex1.Використовуючи функцію filter() вивести тільки парні числа зі списку.

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22]
filtered_numbers = filter(is_even, numbers)

result = list(filtered_numbers)
print(result)

#Ex2.Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.

def contains_a (s):
    return 'a' in s

words = ['apple', 'watch', 'mouse', 'another', 'automation', 'Hello']
filtered_words = filter(contains_a, words)

result_1 = list(filtered_words)
print(result_1)
