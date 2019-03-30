import telebot
import requests
from bs4 import BeautifulSoup
from flask import Flask
import os

TOKEN = '792020505:AAGOyOM4r_If54bNu65kXLXP1mnyIG7Re9E'  # bot
bot = telebot.TeleBot(TOKEN, threaded=False)
server = Flask(__name__)


def traffic_update():
    result = requests.get('https://traffic.nepalpolice.gov.np/index.php/news/traffic-updates/417-update')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    test = soup.select_one('#system > article > div > p')
    # print(test.text)
    return test.text + "\n All information provided by : traffic.nepalpolice.gov.np"


@bot.message_handler(commands=['start'])
def today(m):
    bot.reply_to(m, "तपाई लाई स्वागत छ । Please type 'Update' to get traffic update.\n"
                    "[Still in experimental phase.]")


@bot.message_handler(func=lambda msg: msg.text is not None and 'update' in msg.text or 'Update' in msg.text)
def answer(message):
    bot.reply_to(message, traffic_update())
    print(traffic_update())
    print(message.chat)


@bot.message_handler(func=lambda msg: msg.text is not None)
def answer(message):
    bot.reply_to(message, "Please type 'update' to get more information or see /start")


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_heroku_project.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
