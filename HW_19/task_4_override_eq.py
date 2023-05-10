# Task 4. (optional) Create the User class, which in the constructor should
# accept the name parameter and initialize it into the corresponding attribute.
#
# Redefine the eq method in such a way that when comparing 2 objects of
# the User type in which the name attributes match, we get True. At the
# same time, do not take into account the register in which each of the
# attributes is written.
#
# first_user = User('OLEKSII')
# second_user = User('Oleksii')
# print(first_user == second_user)
# >>> True

class User:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return self.name.upper() == other.name.upper()


first_user = User(input('ENTER FIRST NAME: '))
second_user = User(input('ENTER SECOND NAME: '))

print(f'This user names is {"" if first_user == second_user else "not "}equivalent.')
