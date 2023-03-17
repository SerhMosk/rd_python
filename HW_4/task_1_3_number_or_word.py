# Task 1. Create a program that will expect text input from the user
# and report whether the entered text is a "number" or a "word".
string = input('Please enter something: ')
wordLength = len(string)

print(f'You entered: "{string}"')
print(f'Type of value: {type(string)}')

if wordLength == 0:
    print('You entered empty string.')
elif string.isspace():
    print(f'You entered only space{"s" if wordLength > 1 else ""}.')
elif string.isdigit():
    print('This is a number.')

    # Task 2. If the entered text is "number", the program must also
    # indicate whether it is even or odd.
    if int(string) % 2 == 0:
        print('This number is even.')
    else:
        print('This number is odd.')
elif string.isalpha():
    print('This is a word.')

    # Task 3. If it is a "word", the program must specify its length.
    print(f'This word is {wordLength} character{"s" if wordLength > 1 else ""} long.')
else:
    print('This is a string.')
