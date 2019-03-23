from bot import telegram_chatbot

bot = telegram_chatbot('config.cfg')


def make_reply(msg):
    replies = None
    if msg == 'suson':
        replies =  "Thanks to him I am alive :D"
    if msg is not None:
        replies = bot.get_jokes()
        print(replies)
    return replies

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
        # user_get = updates['result'][0]['message']['chat']['id']
        # msg = updates['result'][0]['message']['text']
        # update_id = updates['result'][0]['update_id']
        # reply = make_reply(msg)
        # bot.send_message(reply, user_get)
        # update_id = update_id + 1
