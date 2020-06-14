import datetime

time = format(datetime.datetime.now())
with open("output.txt", 'a') as output:
    print(time, file=output)


def outputText(text):
    with open("output.txt", 'a') as output:
        print(text, file=output)
