import json
import sys
from telegram.telegrambot import send_message_telegram
from SwoPyApi.swopy import getHomeworkHTML
from SwoPyApi.parser import Parser


def main():

    try:
        with open("../auth/auth.json", "r") as auth:
            options = json.loads(auth.read())
    except:
        print("auth.json not found")
        sys.stderr.write("ERR::COULD NOT FIND HOMEWORK DIV -> PLEASE UPDATE AUTH.JSON\n")
        sys.exit("Programm failed to retrive data")

    html = getHomeworkHTML(options) # Get inner html from swop
    p = Parser(html) # create parser instance

    send_message_telegram(p.getString(), options) # Send message to telegram

    




if __name__ == "__main__":
    main()

    

    

    





