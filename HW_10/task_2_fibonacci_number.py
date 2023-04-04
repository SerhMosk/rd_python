# Task 2. (optional) Create a program that will accept a number and
# print the corresponding number in the Fibonacci sequence using recursion.

def print_fibonacci_sequence(number, lst):
    print(f'The number in Fibonacci Sequence: {number}')
    print(f'The Fibonacci Sequence to the number: {lst}')


def get_fibonacci_number(number, lst=None):
    if lst is None:
        lst = [0]
    lst_len = len(lst)

    if lst_len == 1:
        if number == 0:
            return 0, lst
        else:
            lst.append(1)
            return get_fibonacci_number(number, lst)
    elif lst_len == number + 1:
        return lst[number], lst
    else:
        lst.append(lst[lst_len - 2] + lst[lst_len - 1])
        return get_fibonacci_number(number, lst)


def app_init():
    while True:
        number = input('ENTER NUMBER: ')

        if number.isdigit():
            result = get_fibonacci_number(int(number))
            print_fibonacci_sequence(result[0], result[1])
            break


app_init()
