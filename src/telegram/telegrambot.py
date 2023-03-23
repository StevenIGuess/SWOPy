import telebot


def send_message_telegram(message, options):
    bot = telebot.TeleBot(options['telegramapikey'])
    bot.send_message(chat_id=int(options['telegramchatid']), text=message)

