FROM python:3.9

COPY /devbot ./devbot
COPY /auth ./auth

WORKDIR /devbot/src

RUN pip install pyTelegramBotAPI schedule pymongo selenium webdriver_manager html_to_json aiohttp matplotlib seaborn

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get -y update

RUN apt-get install -y google-chrome-stable

CMD ["python", "./start_dev_bot.py"]