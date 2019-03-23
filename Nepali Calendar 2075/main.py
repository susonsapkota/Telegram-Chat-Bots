#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import time

import telebot
from telebot import types


token = 'This is where token of bot goes'  # testbot

bot = telebot.TeleBot(token, threaded=False)
bot.set_webhook()


def get_date():
    today_date = datetime.datetime.today().strftime('%m/%d/%Y')
    with open('2075.json', 'r', encoding='utf-8') as data_file:
        data = json.load(data_file)
        for months in data:
            for day in months:
                if today_date == day["ad"]:
                    print(day)
                    return day


def today_info(day):
    holidayOrNot = ""

    if day['holiday']:
        holidayOrNot = "Yes, today is holiday :)"
    else:
        holidayOrNot = "No, Today is not holiday :("

    string = "AD : " + day['ad'] + "\nBS : " + day['bs'] + "\nHoliday : " + holidayOrNot + "\nEvent : " + day[
        'event'] + "\nTithi :" + day['tithi']
    return string


def holiday_info(day):
    if day['holiday']:
        holidayOrNot = "Yes, today is holiday :)"
    else:
        holidayOrNot = "No, Today is not holiday :("

    return holidayOrNot


@bot.message_handler(commands=['start'])
def today(m):
    bot.reply_to(m, "तपाई लाई स्वागत छ ।")


@bot.message_handler(commands=['help'])
def today(m):
    bot.reply_to(m, "List of available commands : \n"
                    "/start : to start bot \n"
                    "/help : to list all commands \n"
                    "/month : to get information of whole month\n\n"
                    "or simply type 'today' to get more information about today.\n\n\n"
                    "Do you want to see any feature then email me :D \n"
                    "\n--suson")



@bot.message_handler(func=lambda msg: msg.text is not None and 'today' in msg.text or 'Today' in msg.text)
def answer(message):
    bot.reply_to(message, today_info(get_date()))
    print(message.chat)


@bot.message_handler(func=lambda msg: msg.text is not None and 'holiday' in msg.text or 'Holiday' in msg.text)
def answer(message):
    bot.reply_to(message, holiday_info(get_date()))


@bot.message_handler(func=lambda msg: msg.text is not None and 'suson' in msg.text or 'Suson' in msg.text)
def answer(message):
    bot.reply_to(message, "You found the easter egg, check this out: https://goo.gl/7uHE4H",
                 disable_web_page_preview=True)


@bot.message_handler(commands=['month'])
def answer(message):
    markup = types.ReplyKeyboardMarkup()

    bai = types.KeyboardButton('Baisakh')
    jes = types.KeyboardButton('Jestha')
    ash = types.KeyboardButton('Ashad')
    sawu = types.KeyboardButton('Shrawan')
    bhadau = types.KeyboardButton('Bhadra')
    ashoj = types.KeyboardButton('Ashoj')
    kati = types.KeyboardButton('Kartik')
    mang = types.KeyboardButton('Mangsir')
    posh = types.KeyboardButton('Poush')
    magh = types.KeyboardButton('Magh')
    falg = types.KeyboardButton('Falgun')
    chait = types.KeyboardButton('Falgun')

    markup.row(bai, jes, ash)
    markup.row(sawu, bhadau, ashoj)
    markup.row(kati, mang, posh)
    markup.row(magh, falg, chait)

    bot.send_message(message.chat.id, "Select which month you want to see : ", reply_markup=markup)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Baisakh' in msg.text)
def answer(message):
    photo = open('months/01.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Jestha' in msg.text)
def answer(message):
    photo = open('months/02.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Ashad' in msg.text)
def answer(message):
    photo = open('months/03.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Shrawan' in msg.text)
def answer(message):
    photo = open('months/04.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Bhadra' in msg.text)
def answer(message):
    photo = open('months/05.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Ashoj' in msg.text)
def answer(message):
    photo = open('months/06.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Kartik' in msg.text)
def answer(message):
    photo = open('months/07.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Mangsir' in msg.text)
def answer(message):
    photo = open('months/08.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Poush' in msg.text)
def answer(message):
    photo = open('months/09.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Magh' in msg.text)
def answer(message):
    photo = open('months/10.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Falgun' in msg.text)
def answer(message):
    photo = open('months/11.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None and 'Chaitra' in msg.text)
def answer(message):
    photo = open('months/12.png', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(func=lambda msg: msg.text is not None)
def answer(message):
    bot.reply_to(message, "Please type 'today' to get more information or see /help")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
