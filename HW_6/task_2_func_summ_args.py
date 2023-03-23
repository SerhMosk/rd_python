# Task 2. Create a function that sums any number of arguments and returns the result.

def summ_args(*args):
    summ = 0
    for number in args:
        summ += number
    return summ


result = summ_args(1, 2, 3, 4)
print(f'The sum of the numbers 1, 2, 3, 4 using the function is {result}')

result = summ_args(1, 1, 1, 1, 1)
print(f'The sum of the numbers 1, 1, 1, 1, 1 using the function is {result}')
