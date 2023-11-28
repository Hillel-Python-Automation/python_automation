# Створити конструкції try-except-else

# Write a program,
# when user has 1 child, he can get 20% of discount,
# when user has 2 children, he can get 30% of discount,
# when user has 3 or more children, he can get 50% of discount,
# user without children should pay 100% of price


def child_promotion_int(child_num):
    if child_num == 0:
        print("You can't get any discounts")
    elif child_num == 1:
        print("You can get 20% of discount")
    elif child_num == 2:
        print("You can get 30% of discount")
    elif 3 <= child_num <= 5:
        print("You can get 50% of discount")
    else:
        print("You can get 80% of discount")


def child_promotion_word(child_num_str):
    if child_num_str == "zero":
        print("You can't get any discounts")
    elif child_num_str == "one":
        print("You can get 20% of discount")
    elif child_num_str == "two":
        print("You can get 30% of discount")
    elif child_num_str == "three" or \
            child_num_str == "four" or \
            child_num_str == "five":
        print("You can get 50% of discount")
    else:
        print("You can get 80% of discount")


child = input("Enter how many children do you have? ")

if child == '':
    raise RuntimeError("Input can't be empty!")

try:
    child_num = int(child)
    child_promotion_int(child_num)
except ValueError:
    child_promotion_word(child)
    print("Congratulation with our discount")
else:
    print("Congratulation with our discount")







