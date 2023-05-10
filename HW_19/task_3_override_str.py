# Task 3. (optional) Create a MyStr(str) class, which should override
# the str method so that instead of printing the actual value, all
# letters are converted to uppercase:
# my_str = MyStr('test')
# print(my_str)
# >>> "TEST"

class MyStr:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text.upper()

# class MyStr(str):
#     def __str__(self):
#         return self.upper()


my_str = MyStr(input('ENTER SOME TEXT: '))
print(my_str)
