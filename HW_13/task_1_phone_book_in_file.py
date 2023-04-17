# Task 1. Use the file as a database to store phonebook entries from previous tasks.
# Your phonebook, previously contained in a dict, should be stored as text in JSON format.
# When closing the program and opening it again, all previous data should be available.
# Hint: You can use the json library, which will help with converting dict to JSON string
# (when writing to a file) and JSON string to dict (when reading from a file).
# The file should be updated after each successful add or delete operation.
import json

phone_book_file_path = "phone_book.json"


def read_phone_book():
    try:
        with open(phone_book_file_path) as handler:
            return json.loads(handler.read())

    except IOError:
        print("The phone book file didn't exist and was created!")

        with open(phone_book_file_path, "w") as file_handler:
            file_handler.write("[]")
            return []


def write_phone_book(data, info):
    try:
        with open(phone_book_file_path, "w") as file_handler:
            json_str = json.dumps(data)
            file_handler.write(json_str)
            print(info)

    except IOError:
        print("An IOError has occurred! Try again later.")


def print_info(text=None):
    if text:
        print(text)
    print("Available commands:")
    print(" help or info: list of commands")
    print(" stats: number of records")
    print(" list: list of all names in the book")
    print(" add: add a record")
    print(" show <name>: detailed information by name")
    print(" delete <name>: delete record by name")
    print(" exit: exit from program")


def print_number_of_records():
    book = read_phone_book()
    print(f"Number of phone book records: {len(book)}")


def print_name_list():
    book = read_phone_book()
    if len(book):
        print("The phone book records:")
        for record in book:
            print(f"- {record.get('name')}")
    else:
        print("The phone book is empty. Try adding a new record.")


def find_record(name, show_info=False, return_index=False):
    book = read_phone_book()
    found_record = None
    i = 0

    for record in book:
        if record.get('name') == name:
            found_record = record
            break
        i += 1

    if show_info and found_record is None:
        print(f'No record found with the name "{name}" to show.')

    if return_index:
        return found_record, i

    return found_record


def add_record():
    print("Enter the data below to create a new record.")

    while True:
        name = input('Enter name: ')

        if len(name) == 0:
            print('You entered empty string. Try again.')
            continue
        elif find_record(name) is None:
            break
        else:
            print('This name exists! Try a different name.')

    age = 0
    verified = False
    while True:
        try:
            age = int(input('Enter age: '))
        except ValueError as error:
            print(f' Value Error: {error}')
        else:
            if 3 < age <= 120:
                verified = True
                break
        finally:
            if not verified:
                print('You need to enter the number of years not lees than 4 and not more than 120 years. Try again.')

    while True:
        sex = input('Enter sex: ')
        if sex == 'male' or sex == 'female':
            break
        else:
            print('You can enter "male" or "female". Try again.')

    verified = False
    while True:
        phone = input('Enter phone number: ')
        try:
            if int(phone) and len(phone) >= 10:
                verified = True
                break
        except ValueError as error:
            print(f' Value Error: {error}')
        except Exception as error:
            print(f' Error: {error}')
        finally:
            if not verified:
                print('You need to enter a phone number with a length of at least 10 digits. Try again.')

    book = read_phone_book()
    book.append({"name": name, "age": age, "sex": sex, "phone": phone})
    write_phone_book(book, "New record successfully added.")


def show_record(found_record):
    if found_record:
        print("The record details:")
        print(f" Name: {found_record.get('name')}")
        print(f" Age: {found_record.get('age')}")
        print(f" Sex: {found_record.get('sex')}")
        print(f" Phone number: {found_record.get('phone')}")


def delete_record(name):
    book = read_phone_book()
    result = find_record(name, return_index=True)

    if result[0] is not None:
        del book[result[1]]
        write_phone_book(book, f'The record "{name}" has been deleted.')
    else:
        print(f'No record found with the name "{name}" to delete.')


def init_app():
    print('--- PHONE BOOK ---')
    print('Enter "help" to show commands')

    while True:
        command = input('ENTER COMMAND: ')

        if command == '':
            continue

        elif command == 'exit':
            break

        elif command == 'info' or command == 'help':
            print_info(text='PHONE BOOK PROGRAM')

        elif command == 'stats':
            print_number_of_records()

        elif command == 'list':
            print_name_list()

        elif command == 'add':
            add_record()

        else:
            args = command.split()
            command = args[0]

            if len(args) == 2:
                name = args[1]

                if command == 'show':
                    show_record(find_record(name, show_info=True))

                elif command == 'delete':
                    delete_record(name)

                else:
                    print_info(text='Wrong command.')

            elif command == 'show' or command == 'delete':
                print_info(text='You did not enter the second command parameter <name> without spaces.')

            else:
                print_info(text='Wrong command.')


# Run program
init_app()
