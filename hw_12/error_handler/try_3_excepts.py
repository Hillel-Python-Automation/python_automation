# Створити конструкції try-except з більше ніж трьома except`ами

# Write a program when user should guess a number
class EntranceError(Exception):
    ...


class WrongNumError(Exception):
    ...


class BigNumberError(Exception):
    ...


def guess_a_number(user_number):
    if user_number == guess_num:
        print("Bingo!")
    elif user_number == 24 or user_number == 26:
        raise EntranceError("You are close")
    elif user_number > 100:
        raise BigNumberError("Try to enter number from 1 to 100")
    else:
        raise WrongNumError("Try one more time")


try:
    guess_num = 25
    user_number = int(input("Enter your number: "))
    guess_a_number(user_number)
except ValueError as v:
    print(f"Please enter an integer: {v}")
except EntranceError as e:
    print(f"Error, but {e}")
except WrongNumError as w:
    print(f"Error, {w}")
except BigNumberError as b:
    print(f"Error, {b}")
