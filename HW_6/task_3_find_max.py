# Task 3. (optional) Find the largest element of the array
# — use the built-in function
# — create your own function
# — use the lambda function

some_array = [1, 3, 9, 2, -5, 7, 0]


def get_max(array):
    max_value = array[0]
    for item in array:
        if item > max_value:
            max_value = item
    return max_value


if __name__ == '__main__':
    max_elem = lambda array: max(array)

    print(f'The maximum value in the array {some_array}:')
    print(f'- with the built-in function is {max(some_array)}')
    print(f'- with my function is {get_max(some_array)}')
    print(f'- with the lambda function is {max_elem(some_array)}')
