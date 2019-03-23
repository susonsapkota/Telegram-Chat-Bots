import json
import requests


def get_jokes():
    url = 'https://api.yomomma.info/'
    url = str(url).replace(" ", "+")  # just in case, no space in url
    try:
        page = requests.get(url)
        get_joke = json.loads(page.content)
        return get_joke['joke']
    except requests.HTTPError:
        print("Error while parsing URL")

    return ''


print(get_jokes())

# website = "https://api.telegram.org/bot"
# token = '793587458:AAEjI7ni3JVvOMZPo9JQVv6WPMV9AEOFI18'
# updates = (website + '/getupdates') + token
#
# data = json.loads(file_get_contents(updates))
# get_chat_id = (str(data['result'][0]['message']['chat']['id']))
# get_chat_user = data['result'][0]['message']['chat']['first_name']
# get_msg = data['result'][0]['message']['text']
# joke_website = 'https://api.yomomma.info/'
# joke_api = json.loads(file_get_contents(joke_website))
#
# joke = joke_api['joke']
#
# send_msg = website + '/sendmessage?chat_id=' + get_chat_id + '&text=' + joke
#
# file_get_contents(send_msg)
