print("\n1." + "-" * 30)


def sum_range(start, end):
    """
    1. Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
    Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями. (35 балів)
    """
    if isinstance(start, int) and isinstance(end, int):
        result = 0
        if end < start:
            start, end = end, start
        for item in range(start, end + 1):
            result += item
        return result
    return None


print(f"Sum of items in range(1, 2) = {sum_range(1, 2)}.")
print(f"Sum of items in range(2, 1) = {sum_range(2, 1)}.")
print(f"Sum of items in range(0, 5) = {sum_range(0, 5)}.")
print(f"Sum of items in range(-2, 2) = {sum_range(-2, 2)}.")
print(f"Sum of items in range(-1.0, 1.0) = {sum_range(-1.0, 1.0)}.")
print(f"Sum of items in range(str, str) = {sum_range('str', 'str')}.")
print("\n2." + "-" * 30)


def season(month_number):
    """
    2. Написати функцію season, що приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року,
    якому цей місяць належить (зима, весна, літо чи осінь). (20 балів)
    """
    match month_number:
        case 1 | 2 | 12:
            return "winter"
        case 3 | 4 | 5:
            return "spring"
        case 6 | 7 | 8:
            return "summer"
        case 9 | 10 | 11:
            return "fall"
        case _:
            return None


for item in range(0, 14):
    match item:
        case 1:
            print(f"Season for {item}-st month is {season(item)}.")
        case 2:
            print(f"Season for {item}-nd month is {season(item)}.")
        case _:
            print(f"Season for {item}-th month is {season(item)}.")

print("\n3." + "-" * 30)


def get_filtered(list_arg):
    """
    3. Написати функцію get_filtered(), що приймає 1 аргумент - список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
    і виводить на консоль всі елементи які менші 5. (for/while + if) (20 балів)
    """
    for item in list_arg:
        if item < 5:
            print(f"The {item} is less then 5.")


get_filtered(list_arg=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
print("\n4." + "-" * 30)


def mun1(x):
    """
    4. Написати функцію num1 яка приймає один аргумент x і повертає функцію вкладену функцію, а також має вкладену функцію
    num2 яка приймає один аргумент y і повертає результат множення. (виклик буде num1(3)(4)) (25  балів)
    """
    def mun2(y):
        return x * y

    return mun2


print(f"Nested function: {mun1(3)(4)}.")
print("-" * 30)
