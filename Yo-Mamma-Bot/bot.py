import configparser
import json

import requests


class telegram_chatbot(object):

    def __init__(self, config):
        self.token = self.read_token(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendmessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    def read_token(self, config):
        parser = configparser.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')

    def get_jokes(self):
        url = 'https://api.yomomma.info/'
        url = str(url).replace(" ", "+")
        try:
            page = requests.get(url)
            get_joke = json.loads(page.content)
            return get_joke['joke']
        except ImportError:
            print("Error while importing URL")

        return ''
