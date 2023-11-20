# Використовуючи функцію filter() вивести тільки парні числа зі списку.
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def even_numbers(number):
    if number % 2 == 0:
        return True
    else:
        return False


evens = filter(even_numbers, list_of_numbers)

for number in evens:
    print(number)

# Використовуючи функцію filter() вивести тільки елементи які мають літеру 'а'.

words = ['banana', 'cherry', 'orange', 'month']

words_with_a = list(filter(lambda word: 'a' in word, words))
