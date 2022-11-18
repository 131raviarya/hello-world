import telebot

TOKEN2 = '5577708184:AAHR7BlxQtbBz5848_ejzJ7-MCz8Vd72-yc'

bot = telebot.TeleBot(TOKEN2)

def func():
    @bot.message_handler(content_types="text")
    def sender(message):
        name = str('' if message.from_user.first_name is None else message.from_user.first_name) + \
               str('' if message.from_user.last_name is None else ' ' + message.from_user.last_name)
        id = message.chat.id
        msg = message.text
        bot.send_message(id, f'{name}\n{id}\n{msg}')

    bot.polling()


func()
