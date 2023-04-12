# Task 1. Write your own decorator, the task of which should be
# to print the name of the function and the time when it was called.
# The decorator should work the same for different functions.
import datetime as dt


def decorator_func_name(func):
    print(f'Initialized function with name: {func.__name__}')
    print(f'Time: {dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")}\n')

    def wrapper():
        func()

    return wrapper


@decorator_func_name
def my_func_1():
    print("My func 1")


@decorator_func_name
def my_func_2():
    print("My func 2")


my_func_1()
my_func_2()
