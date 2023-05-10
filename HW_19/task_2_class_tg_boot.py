# Task 2. Create the TelegramBot class, which must be inherited from Bot and must contain:
# - custom attributes url, chat_id (None by default)
# - send_message, set_url and set_chat_id methods.
#
# These methods, except self, must accept 1 parameter (url and chat_id respectively)
# and assign the value of this parameter to the url and chat_id attributes respectively.
#
# TelegramBot should also override the send_message method to print the value
# of the message parameter with any supporting text. This text must also contain
# the url and chat_id values.
#
# The result should be:
# some_bot = Bot('Marvin')
# some_bot.say_name()
# >>> "Marvin"
#
# some_bot.send_message("Hello")
# >>> "Hello"
#
# telegram_bot = TelegramBot("TG")
# telegram_bot.say_name()
# >>> "TG"
#
# telegram_bot.send_message('Hello')
# >>> "TG bot says Hello to chat None using None"
#
# telegram_bot.set_chat_id(1)
# telegram_bot.send_message('Hello')
# >>> "TG bot says Hello to chat 1 using None"

import task_1_class_bot as class_bot


class TelegramBot(class_bot.Bot):
    url = None
    chat_id = None

    def send_message(self, message):
        print(f'{self.name}\'s bot says {message} to chat {self.chat_id} using url {self.url}')

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id


def init_app():
    print('=== Telegram Bot ===\nFor stop program enter "exit"')

    while True:
        name = input('BOT: Enter your name: ')

        if name == 'exit':
            break
        elif name == '':
            continue

        bot = TelegramBot(name)

        print('BOT: Your name is ', end='')
        bot.say_name()

        print('-'*30)
        while True:
            with_url = input('BOT: You have URL? (yes|no): ')
            if with_url == 'yes':
                bot.set_url(input('BOT: Enter URL: '))
                break
            elif with_url == 'no':
                break

        print('-'*30)
        while True:
            with_chat_id = input('BOT: You have chat_id? (yes|no): ')
            if with_chat_id == 'yes':
                bot.set_chat_id(input('BOT: Enter chat_id: '))
                break
            elif with_chat_id == 'no':
                break

        print('-'*30)
        bot.send_message(input('BOT: Enter your message: '))
        print('='*30)


if __name__ == "__main__":
    init_app()
