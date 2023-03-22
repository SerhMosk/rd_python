# Task 1. Create a function that takes an argument to a power and returns it,
# the power must also be an argument.

print('Raising the number to a power')

base_number = int(input('Enter the number: '))
power_number = int(input('Enter the power of the number: '))


def pow_number(number, power):
    return number ** power


pow_result = pow_number(base_number, power_number)

print(f'The result of raising the number {base_number} to the power of {power_number} is {pow_result}')
