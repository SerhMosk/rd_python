# Task 1. Create a program that will expect the user to enter text
# and output information for each typed character:
# - this "number" + what it is (even, odd),
# - this is a "letter" + what is it (uppercase or lowercase),
# - is a "symbol"

string = input('Please enter something: ')
print(f'You entered: "{string}"')

for char in string:
    if char.isdigit():
        if int(char) % 2 == 0:
            print(f'{char} - even number')
        else:
            print(f'{char} - odd number')
    elif char.isalpha():
        if char.islower():
            print(f'{char} - lowercase letter')
        else:
            print(f'{char} - uppercase letter')
    elif char.isspace():
        print(f'{char} - space')
    else:
        print(f'{char} - symbol')
