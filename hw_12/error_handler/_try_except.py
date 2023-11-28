# 4. Створити конструкції try-except для арифметичної операції, роботи з
# колекціями.



try:
    users = [1, 2]
    num = int(input("Enter your num: "))

    print(users + num)
    # check_sum_odd(num_1, num_2)
    # print(result)

except ValueError:
    print("(Invalid input. Please enter valid data in field of prompt)")
except TypeError:
    print("Can't add")



