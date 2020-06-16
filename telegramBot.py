import getFile
import requests as requests
import os


def send_message(message, sendId):
    telegramAPI = getFile.getListFile('apiTelegram.txt')
    params = {"chat_id": telegramAPI[sendId], 'text': message}
    response = requests.post(telegramAPI[0]+'sendMessage', data=params)
    os.remove('output.txt')
