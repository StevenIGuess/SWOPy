import json
import time
from datetime import datetime
import schedule
from logs.logger import crashreport
from telegram.telegrambot import send_message_telegram
from SwoPyApi.swopy import getHomeworkHTML
from SwoPyApi.parser import Parser


def main():

    try:
        with open("../auth/auth.json", "r") as auth:
            options = json.loads(auth.read())
    except:
        crashreport("COULD NOT OPEN AUTH")

    try:
        html = getHomeworkHTML(options) # Get inner html from swop
        p = Parser(html) # create parser instance
    except:
        crashreport("COULD NOT GET DATA -> PLEASE UPDATE AUTH.JSON")


    send_message_telegram(p.getString(), options) # Send message to telegram


if __name__ == "__main__":
    schedule.every().friday.at("18:00").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
        

    

    

    





