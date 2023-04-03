# Both iterators and generators are used in Python for iterating
# over a sequence of values.
# However, there are some differences between the two:
#
# 1. Definition: An iterator is an object that implements the
#    iterator protocol, which consists of the iter() and next() methods.
#    On the other hand, a generator is a function that uses the yield
#    keyword to return a generator object.
#
# 2. Usage: Iterators are used for traversing a container, while generators
#    are used for creating an iterable sequence.
#
# 3. Execution: Iterators execute immediately and return a result,
#    while generators execute lazily, producing a sequence of values as
#    requested.
#
# 4. State: An iterator can only be iterated once and then it's exhausted,
#    while a generator can be iterated over multiple times as it maintains
#    its state between iterations.
#
# 5. Memory: Iterators require more memory as they store all the values
#    in memory at once, while generators are more memory-efficient as
#    they generate values on the fly.
#
# In summary, iterators are objects that implement the iterator protocol
# and are used for traversing a container, while generators are functions
# that use the yield keyword to create an iterable sequence.
#
# Generators are often more memory-efficient and can be iterated over
# multiple times, while iterators are typically used when you need to
# iterate over a sequence only once.
import os
import random
from sys import getsizeof

# ===== Simple iterator
string = "I love Python"


def simple_iterator(usage):
    if usage == 'iter_simple':
        string_iterator = iter(string)  # create an iterator

        print(type(string_iterator))

        print(next(string_iterator))
        print(next(string_iterator))
        print(next(string_iterator))
        print(next(string_iterator))
        print(next(string_iterator))
        print(next(string_iterator))
    elif usage == 'iter_in_for':
        # item == next(string)
        for item in string:
            print(item)
    elif usage == 'iter_print':
        print(next(iter(string)))


def list_iteration():
    my_list = [0, 1, 2, 3, 4, 5]

    list_iterator = iter(my_list)

    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))


# ===== Simple generator
def generator_function(size):
    value = 0
    while value < size:
        yield value
        value += 1


def simple_generator(usage):
    gen = generator_function(5)
    if usage == 'gen_simple':
        print(generator_function)
        print(gen)

    elif usage == 'gen_in_for':
        # item == next(gen)
        for item in gen:
            print(item)

    elif usage == 'gen_print':
        print(next(gen))
        print(next(gen))
        print(next(gen))
        print(next(gen))
        print(next(gen))


# ===== Custom iterator
class MyIterator:
    value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == 6:
            raise StopIteration()

        result = self.value
        self.value += 1
        return result


def custom_iterator():
    my_iterator_object = MyIterator()
    print(my_iterator_object)

    print(next(my_iterator_object))

    for item in my_iterator_object:
        print(item)

    print('Iteration is over')


# ===== Iterating over files in a directory:
class FileIterator:
    def __init__(self, path):
        self.path = path
        self.files = os.listdir(path)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration

        file_name = self.files[self.index]
        self.index += 1
        return file_name


def directory_iteration():
    dir_iter = FileIterator("./")
    for file in dir_iter:
        print(file)


# ===== Infinite generator
def random_numbers():
    # Loop is required here!!!
    while True:
        yield random.randint(1, 100)


def infinity_generator():
    rand_gen = random_numbers()
    for _ in range(10):
        print(next(rand_gen))


# ===== Read large files
def read_large_file(file_path, chunk_size=1024):
    with open(file_path) as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


def chunk_iteration():
    reader = read_large_file("./large_file.txt", 5)
    for _ in range(3):
        print(next(reader))


# ===== Generator Expression
def generator_expression(usage):
    lst = range(10)
    data = {"one": 1, "two": 2}

    gen_lst = [f for f in lst]
    gen = (f for f in lst)
    gen_set = {f for f in lst}
    gen_dict = {key: value for key, value in data.items() if value != 1}

    if usage == 'genex_print':
        print(gen_lst)
        print(gen)
        print(gen_set)
        print(gen_dict)
    elif usage == 'genex_types':
        print(type(gen_lst))
        print(type(gen))
        print(type(gen_set))
        print(type(gen_dict))


def get_sizeof():
    lst = range(2 ** 24)

    print(getsizeof([f for f in lst]))
    print(getsizeof((f for f in lst)))
    print(getsizeof({f for f in lst}))
    print(getsizeof({f: f for f in lst}))


# # !!! Advanced topic: yield from
def sub_generator():
    for i in range(3):
        yield i


def main_generator():
    yield from sub_generator()
    yield 'Done'


def yield_from():
    for val in main_generator():
        print(val)


def print_info(text=None):
    if text:
        print(text)
    print("Available commands:")
    print(" help or info: list of commands")
    print(" iter_simple: simple iterator")
    print(" iter_in_for: iterator in for ... in")
    print(" iter_print: print first iteration")
    print(" iter_list: list iteration wit iterator")
    print(" iter_custom: custom iterator")
    print(" iter_directory: directory iterator")
    print(" iter_file_chunks: file chunks iterator")
    print(" gen_simple: simple generator")
    print(" gen_in_for: generator in for ... in")
    print(" gen_print: generator items print")
    print(" gen_infinity: infinity generator")
    print(" genex_print: generator expressions print")
    print(" genex_types: generator expressions print types")
    print(" iter_sizeof: generator and iterable types sizeof")
    print(" gen_yield_from: advanced topic - yield from")
    print(" exit: exit from program")


def init_app():
    print('--- ITERATORS & GENERATORS ---')
    print('Enter "help" to show commands')

    while True:
        command = input('ENTER COMMAND: ')

        if command == '':
            continue

        elif command == 'exit':
            break

        elif command == 'info' or command == 'help':
            print_info(text='ITERATORS & GENERATORS EXAMPLES')

        elif command == 'iter_simple' or command == 'iter_in_for' or command == 'iter_print':
            simple_iterator(command)
        elif command == 'iter_list':
            list_iteration()
        elif command == 'gen_simple' or command == 'gen_in_for' or command == 'gen_print':
            simple_generator(command)
        elif command == 'gen_infinity':
            infinity_generator()
        elif command == 'iter_custom':
            custom_iterator()
        elif command == 'iter_directory':
            directory_iteration()
        elif command == 'iter_file_chunks':
            chunk_iteration()
        elif command == 'genex_print' or command == 'genex_types':
            generator_expression(command)
        elif command == 'iter_sizeof':
            get_sizeof()
        elif command == 'gen_yield_from':
            yield_from()


init_app()
