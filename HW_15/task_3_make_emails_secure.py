# Task 3. (optional) Write a program that will:
# - read text from a file whose name is entered by the user (program argument or input)
# - find all emails in the text and change them to X***@****X, where X should be replaced by
# the first and last letters of the real address, and all other text should be replaced by *.
# The number of * does not necessarily have to correspond to the number of replaced characters.
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


def secure_emails(content):
    results = re.findall(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}", content)

    for item in results:
        data = item.split('@')
        secured_email = data[0][0] + "*" * (len(data[0]) - 1) + "@" + "*" * (len(data[1]) - 1) + data[1][-1]

        content = re.sub(item, secured_email, content)
        # content = content.replace(item, secured_email)

    return content


def init_app():
    while True:
        print("Secure email addresses on file with pattern X***@****X")
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
    file_text = secure_emails(file_text)
    print("After changes:")
    print(file_text)
    write_to_file(filename, file_text)


init_app()
