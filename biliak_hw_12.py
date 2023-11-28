# 4. Створити конструкції try-except для арифметичної операції, роботи з
# колекціями.


# Enter two numbers, the sum of which should be even
def check_sum_odd(num_1, num_2):
    if (num_1 + num_2) % 2 == 0:
        print(f"The result of operation '({num_1} + {num_2}) % 2' is even")

    else:
        print(
            f"The result of operation '({num_1} + {num_2}) % 2' is odd. Try to enter another numbers in "
            f"your inputs to get even result")


try:
    num_1 = int(input("Enter your first num: "))
    num_2 = int(input("Enter your second num: "))

    check_sum_odd(num_1, num_2)
    # print(result)

except ValueError:
    print("(Invalid input. Please enter valid data in field of prompt)")



