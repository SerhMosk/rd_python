# Task 1. Add error handling to the code from task #7 about the phone book
# (topic: "Collections and data structures. Part 1")
#
# There should be at least two try except blocks, you decide where to use them.


init_phone_book = [
    {"name": "Serhiy", "age": "40", "sex": "male", "phone": "0961111111"},
    {"name": "Vitalii", "age": "35", "sex": "male", "phone": "0962222222"}
]


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


def print_number_of_records(book):
    print(f"Number of phone book records: {len(book)}")


def print_name_list(book):
    print("The phone book records:")
    for record in book:
        print(f"- {record.get('name')}")


def find_record(book, name, show_info=False, return_index=False):
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


def add_record(book):
    print("Enter the data below to create a new record.")

    while True:
        name = input('Enter name: ')

        if len(name) == 0:
            print('You entered empty string. Try again.')
            continue
        elif find_record(book, name) is None:
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

    book.append({"name": name, "age": age, "sex": sex, "phone": phone})
    print("New record successfully added.")

    return book


def show_record(found_record):
    if found_record:
        print("The record details:")
        print(f" Name: {found_record.get('name')}")
        print(f" Age: {found_record.get('age')}")
        print(f" Sex: {found_record.get('sex')}")
        print(f" Phone number: {found_record.get('phone')}")


def delete_record(book, name):
    result = find_record(book, name, return_index=True)

    if result[0] is not None:
        del book[result[1]]
        print(f'The record "{name}" has been deleted.')
    else:
        print(f'No record found with the name "{name}" to delete.')
    return book


def init_app(phone_book):
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
            print_number_of_records(phone_book)

        elif command == 'list':
            print_name_list(phone_book)

        elif command == 'add':
            phone_book = add_record(phone_book)

        else:
            args = command.split()
            command = args[0]

            if len(args) == 2:
                name = args[1]

                if command == 'show':
                    show_record(find_record(phone_book, name, show_info=True))

                elif command == 'delete':
                    phone_book = delete_record(phone_book, name)

                else:
                    print_info(text='Wrong command.')

            elif command == 'show' or command == 'delete':
                print_info(text='You did not enter the second command parameter <name> without spaces.')

            else:
                print_info(text='Wrong command.')


# Run program
init_app(init_phone_book)
