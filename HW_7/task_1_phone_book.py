# Task 1. Create a phone book that will have the following commands:
# stats: number of records
# add: add a record
# delete <name>: delete record by name (key)
# list: list of all names in the book
# show <name>: detailed information by name
#
# Entries must not be repeated, it is forbidden to overwrite entries,
# only delete and add again.

init_phone_book = [
    {"name": "Serhiy", "age": "40", "sex": "man", "phone": "0961111111"},
    {"name": "Vitalii", "age": "35", "sex": "man", "phone": None}
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

        if find_record(book, name) is None:
            break
        else:
            print('This name exists! Try a different name.')

    age = input('Enter age: ')
    sex = input('Enter sex: ')
    phone = input('Enter phone number: ')

    book.append({"name": name, "age": age, "sex": sex, "phone": "-" if phone == "" else phone})
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
