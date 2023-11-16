class CustomException(BaseException):
    pass


while True:
    value1 = input("Enter value1: ")
    if value1.lower() == 'exit':
        break
    value2 = input("Enter value2: ")
    if value2.lower() == 'exit':
        break

    try:
        value1 = float(value1)
        value2 = float(value2)
        print(value1/value2)
    except ZeroDivisionError as zde:
        print("Please be careful you have got '{}' error".format(zde))
    except ArithmeticError as ae:
        print(ae)
    except ValueError as ve:
        # print("Please be careful you have got '{}' error".format(ve))
        raise CustomException("Please be more accurate with the data you are providing: {}".format(ve))
    except Exception as ex:
        print("Please fix your errors")
    else:
        print("everything went well")
        break
    finally:
        print(f"The inputted values were value1: {value1} and value2: {value2}")


# try-except
try:
    print(5/0)
except Exception:
    print("Handle this")


# try-except-finally
try:
    print(5/0)
except Exception:
    print("Handle error")
finally:
    print("Finalizing the block")


# try-except-else
try:
    print(5/0)
except Exception:
    print("Handle error")
else:
    print("Else block")


# try-except-else-finally
try:
    print(5/0)
except Exception:
    print("Handle error")
else:
    print("Else block")
finally:
    print("Finalizing the block")
