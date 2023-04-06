# Task 2. (optional) Write a custom Exception class, MyCustomException,
# which should report "Custom exception is occurred".

class MyCustomException(Exception):
    pass


while True:
    number = input('ENTER NUMBER: ')
    try:
        if not number.isdigit():
            raise MyCustomException('Custom exception is occurred. This not a number. Try again.')
    except MyCustomException as error:
        print(error)
    else:
        print(f'You entered number: {number}')
        break
