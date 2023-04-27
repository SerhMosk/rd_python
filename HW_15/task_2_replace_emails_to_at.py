# Task 2. (optional) Write a program that will:
# - read text from a file whose name is entered by the user (program argument or input)
# - find all emails in the text and change them to *@*.
import re


def read_file(filename):
    try:
        with open(filename) as handler:
            return handler.read()

    except IOError:
        print("The file didn't exist!")
        return None


def write_to_file(filename, content):
    try:
        with open(filename, "w") as file_handler:
            file_handler.write(content)

    except IOError:
        print("An IOError has occurred! Try again later.")


def replace_emails(content):
    return re.sub(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}", "*@*", content)


def init_app():
    print("Replace email addresses on file to *@*")
    while True:
        filename = input("ENTER FILENAME: ")

        if re.fullmatch(r'^\w+(\.\w{1,5})?$', filename):
            file_text = read_file(filename)
            if file_text is None:
                pass
            elif len(file_text) == 0:
                print("This file is empty.")
            else:
                break
        else:
            print("You need to enter the filename in the format <name>.<ext>.\n"
                  "Where <name> is any word characters and <ext> is extension, max 5 word characters.")

        print("Try again.")

    print("Before changes:")
    print(file_text)
    file_text = replace_emails(file_text)
    print("After changes:")
    print(file_text)
    write_to_file(filename, file_text)


init_app()
