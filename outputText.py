import datetime
import time


def initTime():
    time = format(time.ctime()) + '\n'
    with open("output.txt", 'a') as output:
        print(time, file=output)


def outputText(text):
    with open("output.txt", 'a') as output:
        print(text, file=output)
