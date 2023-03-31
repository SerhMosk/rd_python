# Task 4. (optional) Output all elements of the array that are numbers using filter.

init_lst = [1, 'hello', 'word', True, 100, -10, 0, 1.5, '50']


def is_number(elem):
    return type(elem) == int or type(elem) == float


def get_list_numbers(lst):
    return list(filter(is_number, lst))


numbers_list = get_list_numbers(init_lst)

print(f'Initial list: {init_lst}')
print(f'List of numbers: {numbers_list}')
# Output: [1, 100, -10, 0, 1.5]
