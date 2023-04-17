# Task 2. Write a decorator that will write the name of the function
# it decorates to a file, and write the time of its call.
import datetime as dt

log_file_path = "func_init.log"


def write_to_log(string):
    try:
        with open(log_file_path, "a") as file_handler:
            file_handler.write(string)
            print(string)

    except IOError:
        print("An IOError has occurred! Try again later.")


def decorator_func_name(func):
    write_to_log(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")}: {func.__name__}\n')

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
