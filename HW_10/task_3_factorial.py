# Task 3. (optional) Write a program that will return
# the factorial of the entered number using recursion.

def get_factorial(number):
    if number == 0:
        return 1
    return get_factorial(number - 1) * number


def app_init():
    while True:
        number = input('ENTER NUMBER: ')

        if number.isdigit():
            print(f"The factorial of the number {number} is {get_factorial(int(number))}")
            break


app_init()
