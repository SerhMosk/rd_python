# Task 1. Write a recursion that will print numbers from the user input to zero.

def print_number_to_zero(number):
    print(number)
    if number > 0:
        print_number_to_zero(number - 1)


def app_init():
    while True:
        number = input('ENTER NUMBER: ')

        if number.isdigit():
            print_number_to_zero(int(number))
            break


app_init()
