# Task 5. (optional) Create Bot and TelegramBot classes from
# the first task using the type function

def init_bot(self, name):
    self.name = name


def say_name(self):
    print(self.name)


def send_message(self, message):
    print(f'{self.name}: {message}')


Bot = type(
    'Bot',
    (),
    {
        '__init__': init_bot,
        'say_name': say_name,
        'send_message': send_message,
    }
)


def tg_send_message(self, message):
    print(f'{self.name}\'s bot says {message} to chat {self.chat_id} using url {self.url}')


def set_url(self, url):
    self.url = url


def set_chat_id(self, chat_id):
    self.chat_id = chat_id


TelegramBot = type(
    'TelegramBot',
    (Bot, ),
    {
        'url': None,
        'chat_id': None,
        'set_url': set_url,
        'set_chat_id': set_chat_id,
        'send_message': tg_send_message,
    }
)


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
