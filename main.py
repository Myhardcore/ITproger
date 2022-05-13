import telebot
from random import randint

guess = randint(0, 20)
print(guess)

bot = telebot.TeleBot('5208863521:AAH5L_YiVimwH6M-4PpolzzpCb0hhisLozs')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>, поиграем?'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if int(message.text) > guess:
        bot.send_message(message.chat.id, 'Слишком много')
    elif int(message.text) < guess:
        bot.send_message(message.chat.id, 'Слишком мало')
    elif int(message.text) == guess:
        bot.send_message(message.chat.id, 'Верно!')


bot.polling(none_stop=True)

