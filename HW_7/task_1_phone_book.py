# Task 1. Create a phone book that will have the following commands:
# stats: number of records
# add: add a record
# delete <name>: delete record by name (key)
# list: list of all names in the book
# show <name>: detailed information by name
#
# Entries must not be repeated, it is forbidden to overwrite entries,
# only delete and add again.

def print_info():
    print("Available commands:")
    print(" help or info: list of commands")
    print(" stats: number of records")
    print(" list: list of all names in the book")
    print(" add: add a record")
    print(" show <name>: detailed information by name")
    print(" delete <name>: delete record by name")
    print(" exit: exit from program")


phone_book = [
    {"name": "Serhiy", "age": "40", "sex": "man", "phone": "0961111111"},
    {"name": "Vitalii", "age": "35", "sex": "man", "phone": None}
]

print('--- PHONE BOOK ---')
print('Enter "help" to show commands')

while True:
    command = input("ENTER COMMAND: ")

    if command == "":
        continue

    elif command == 'exit':
        break

    elif command == "info" or command == "help":
        print("PHONE BOOK PROGRAM")
        print_info()

    elif command == "stats":
        print(f"Number of phone book records: {len(phone_book)}")

    elif command == 'list':
        print("The phone book records:")
        for user in phone_book:
            print(f"- {user.get('name')}")

    elif command == 'add':
        print("Enter the data below to create a new record.")
        while True:
            name = input('Enter name: ')
            is_available = True

            for user in phone_book:
                if user.get('name') == name:
                    is_available = False
            if is_available:
                break
            else:
                print('This name exists! Try a different name.')

        age = input('Enter age: ')
        sex = input('Enter sex: ')
        phone = input('Enter phone number: ')

        phone_book.append({"name": name, "age": age, "sex": sex, "phone": "-" if phone == "" else phone})
        print("New record successfully added.")

    else:
        args = command.split()
        command = args[0]

        if len(args) == 2:
            name = args[1]
            found_user = None

            if command == 'show':
                for user in phone_book:
                    if user.get('name') == name:
                        found_user = user
                        break

                if found_user:
                    print("The record details:")
                    print(f" Name: {found_user.get('name')}")
                    print(f" Age: {found_user.get('age')}")
                    print(f" Sex: {found_user.get('sex')}")
                    print(f" Phone number: {found_user.get('phone')}")
                else:
                    print(f'No record found with the name "{name}" to show.')

            elif command == 'delete':
                i = 0
                for user in phone_book:
                    if user.get('name') == name:
                        found_user = user
                        break
                    i += 1

                if found_user:
                    del phone_book[i]
                    print(f'The record "{name}" has been deleted.')
                else:
                    print(f'No record found with the name "{name}" to delete.')

            else:
                print('Wrong command.')
                print_info()

        elif command == 'show' or command == 'delete':
            print('You did not enter the second command parameter <name> without spaces.')
            print_info()

        else:
            print('Wrong command.')
            print_info()
