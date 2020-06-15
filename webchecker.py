import urllib.request
import urllib.error
import os
import datetime
import getFile
import outputText
from telegramBot import send_message
# from tcp_latency import measure_latency


def checkLatency(hostname):
    """
    1. hostname = hostname ex. madiunkota.go.id
    check latency from hostname using os.system for linux -c 
    """
    latency = os.system('ping -c 3 -q -n ' + hostname)
    return latency


def webChecker(website):

    link = getFile.getListFile('listWeb/' + website + '.txt')

    for link in link:
        try:
            r = urllib.request.urlopen("http://"+link)
        except Exception as e:
            """
            Check Error by Code
            """
            # telegramBot.send_message('error')
            outputText.outputText(
                link + " ❌ \n" + str(e))

        if r.getcode() == 200:
            outputText.outputText(link + " ✅")
            # checkLatency(link)
            # print(measure_latency(host=url))
        else:
            """
            Check Error by Status Code
            """
            outputText.outputText(
                link + " ❌ \nError Code " + format(r.getcode()))
    message = open(r"output.txt", 'r')
    send_message(message.read())
