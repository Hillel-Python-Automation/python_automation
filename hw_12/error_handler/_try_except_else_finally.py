
def guess_number(guess_input, guess_num):

    if guess_num == guess_input:
        print("Bingo")
    elif guess_input > guess_num:
        print("Too large")
    else:
        print("Too small")


while True:
    try:
        guess_input = int(input("Enter your number: "))
        guess_num = 10
        guess_number(guess_input, guess_num)

    except ValueError:
        print(f"Invalid input. Check your entered data and enter a number")
    else:
        print("Hoped you got pleasure to play with me!")
    finally:
        print("Want to play again?")

