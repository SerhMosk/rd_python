# Task 4 (optional). Create a program that will wait for text input from the user and
# report what type of data is entered. Use match, case and Python's built-in functions.


def type_of_var(var):
    var_type = str(type(var))

    match var_type:
        case "<class 'bool'>":
            return 'boolean'
        case "<class 'int'>":
            return 'integer'
        case "<class 'float'>":
            return 'float'
        case "<class 'complex'>":
            return 'complex'
        case "<class 'list'>":
            return 'list'
        case "<class 'range'>":
            return 'range'
        case "<class 'str'>":
            return 'string'
        case "<class 'NoneType'>":
            return 'NoneType'
        case _:
            return 'unknown'


# Other solution
def detect_type(var):
    match var:
        case bool():
            return 'boolean'
        case int():
            return 'integer'
        case float():
            return 'float'
        case complex():
            return 'complex'
        case list():
            return 'list'
        case range():
            return 'range'
        case str():
            return 'string'
        case None:
            return 'NoneType'
        case _:
            return 'unknown'


some_var = input('Please enter something: ')

print(f'You entered: "{some_var}"\n')

# Used type_of_var()
print('FIRST SOLUTION')
print(f'Type of input: {type_of_var(some_var)}', end='\n\n')

print(f'Type of True: {type_of_var(True)}')
print(f'Type of 1: {type_of_var(1)}')
print(f'Type of 1.5: {type_of_var(1.5)}')
print(f'Type of 1j: {type_of_var(1j)}')
print(f'Type of [1, 2]: {type_of_var([1, 2])}')
print(f'Type of range(1): {type_of_var(range(1))}')
print(f'Type of "text": {type_of_var("text")}')
print(f'Type of None: {type_of_var(None)}', end='\n\n')

# Used detect_type()
print('SECOND SOLUTION')
print(f'Type of input: {detect_type(some_var)}', end='\n\n')

print(f'Type of True: {detect_type(True)}')
print(f'Type of 1: {detect_type(1)}')
print(f'Type of 1.5: {detect_type(1.5)}')
print(f'Type of 1j: {detect_type(1j)}')
print(f'Type of [1, 2]: {detect_type([1, 2])}')
print(f'Type of range(1): {detect_type(range(1))}')
print(f'Type of "text": {detect_type("text")}')
print(f'Type of None: {detect_type(None)}')
