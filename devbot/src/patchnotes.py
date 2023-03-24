import telebot
import json

with open("../../auth/auth.json", "r") as auth:
    options = json.loads(auth.read())

with open("../patchnotes.txt", "r") as patchnotes:
    message = patchnotes.read()

bot = telebot.TeleBot(options['telegrammapikey_dev'])
bot.send_message(chat_id=int(options['fakechat']), text=message)