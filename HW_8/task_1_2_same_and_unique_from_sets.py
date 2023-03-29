# Task 1. Write a function that returns only the same elements of two sets.

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}


def duplicates_from_sets(set1, set2):
    # return set1 & set2
    elements = set()

    for elem1 in set1:
        for elem2 in set2:
            if elem1 == elem2:
                elements.add(elem1)
    return elements


duplicates = duplicates_from_sets(set_1, set_2)

print(f'set_1: {set_1}')
print(f'set_2: {set_2}')
print(f'The same elements of two sets: {duplicates}')
# Output: {3, 4, 5}


# Task 2. Write a function that returns only the unique elements of two sets.
def unique_from_sets(set1, set2, only_unique=False):
    # return set1 | set2
    # return set1.symmetric_difference(set2)
    elements = set(set1)

    for elem2 in set2:
        absent = True
        for elem1 in set1:
            if elem1 == elem2:
                if only_unique:
                    elements.remove(elem2)
                absent = False
        if absent:
            elements.add(elem2)
    return elements


unique_elements = unique_from_sets(set_1, set_2)
only_unique_elements = unique_from_sets(set_1, set_2, only_unique=True)

print(f'The unique elements of two sets: {unique_elements}')
# Output: {1, 2, 3, 4, 5, 6, 7}

print(f'Only the unique elements of two sets: {only_unique_elements}')
# Output: {1, 2, 6, 7}
