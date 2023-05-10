# Task 1. Create a Bot class with the name attribute and the say_name and send_message methods.
# send_message should take parameters self and message and should print message.
# The say_name method should print the value of the name attribute.

class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(f'{self.name}: {message}')


def init_app():
    print('=== Class Bot ===\nFor stop program enter "exit"')
    while True:
        name = input('BOT: Enter your name: ')

        if name == 'exit':
            break
        elif name == '':
            continue

        bot = Bot(name)

        print('BOT: Your name is ', end='')
        bot.say_name()

        bot.send_message(input('BOT: Enter your message: '))


if __name__ == "__main__":
    init_app()
