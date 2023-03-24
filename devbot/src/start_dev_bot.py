from telebot.async_telebot import AsyncTeleBot
import asyncio
from graph.grapher import create_plot
from telebot.types import InputFile
import json
import os

if __name__ == '__main__':
    with open("../../auth/auth.json", "r") as auth:
        options = json.loads(auth.read())


    bot = AsyncTeleBot(options['telegrammapikey_dev'])

    @bot.message_handler(commands=['help', 'start'])
    async def send_welcome(message):
        await bot.reply_to(message, f"I am SwopBot version {options['version']}\n I can't really do anything that interesting")

    @bot.message_handler(commands=['graph'])
    async def send_graph(message):
        if message.chat.id != int(options['fakechat']):
            await bot.reply_to(message, f"You do not have permission to do that.")
        else:
            try:
                create_plot("../plot.png", options)
                await bot.send_photo(chat_id=int(options['fakechat']), photo=InputFile("../plot.png"), reply_to_message_id=message.message_id)
                os.remove("../plot.png")
            except:
                await bot.reply_to(message, f"Something went wrong.")
    
    asyncio.run(bot.polling())


    