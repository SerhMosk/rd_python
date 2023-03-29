# Task 3. (optional) Convert all list elements of type string to upper case using map.

init_lst = [1, 'hello', 'word', True]


def to_uppercase(elem):
    return elem.upper() if type(elem) == str else elem


def convert_elements_to_uppercase(lst):
    return list(map(to_uppercase, lst))


new_lst = convert_elements_to_uppercase(init_lst)

print(f'Initial list: {init_lst}')
print(f'New list: {new_lst}')
