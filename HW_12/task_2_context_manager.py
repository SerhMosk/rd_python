# Task 2. (optional) Write your own context manager whose
# task will be to print "==========" - 10 characters are
# equal before code execution and after code execution,
# thus highlighting the code block with equals characters.
class DictManager:
    def __enter__(self):
        print("=" * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == KeyError:
            print(f"Sorry! Key {exc_val} does not exist")
        print("=" * 10)
        return True


def check_dict_key(ch_dict):
    print('Enter some key for find value in dictionary or "--s" for stop program.')
    while True:
        key = input('Enter a key: ')

        if key == '--s':
            break
        else:
            print(f'Key "{key}" exists! {key} = {ch_dict[key]}')


init_dict = {'1': 'one', '2': "two"}

with DictManager():
    check_dict_key(init_dict)
