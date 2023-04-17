# Task 3. In the pre-written custom Exception, add a record of
# the error and the time of its occurrence to the file.
import datetime as dt

log_file_path = "errors.log"


class CheckNumberException(Exception):
    pass


def write_to_log(error_msg):
    try:
        with open(log_file_path, "a") as file_handler:
            print(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")}: {error_msg}', file=file_handler)

    except IOError:
        print("An IOError has occurred! Try again later.")


while True:
    number = input('ENTER NUMBER: ')

    try:
        if not number.isdigit():
            raise CheckNumberException(f'"{number}" - this not a number.')

    except CheckNumberException as error:
        write_to_log(error)
        print(error, 'Try again.')

    else:
        print(f'You entered number: {number}')
        break
