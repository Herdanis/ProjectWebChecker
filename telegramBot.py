import getFile
import requests as requests


def send_message():
    telegramAPI = getFile.getListFile('apiTelegram.txt')
    params = {"chat_id": telegramAPI[1], 'text': 'test'}
    response = requests.post(telegramAPI[0]+'sendMessage', data=params)
    return response


send_message()
