# Task 3. (optional) Rewrite the decorator from the first task to accept
# an integer argument `times`. Print function name and time as many
# times as 'times' is specified.
import datetime as dt


def decorator_func_name(times):
    def wrapper(func):
        # First solution
        # text = f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")}: "{func.__name__}" init\n' * times
        # print(text)

        # Second solution
        for _ in range(times):
            print(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")}: "{func.__name__}" init')
        print()

        def inner():
            func()
        return inner
    return wrapper


@decorator_func_name(times=1)
def my_func_1():
    print("My func 1")


@decorator_func_name(times=2)
def my_func_2():
    print("My func 2")


@decorator_func_name(times=3)
def my_func_3():
    print("My func 3")


my_func_1()
my_func_2()
my_func_3()
