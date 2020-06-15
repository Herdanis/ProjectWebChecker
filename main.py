import webchecker
import time
# import webcheckerIntent
import schedule
import time


# print(time.ctime())

webchecker.webChecker('test')


def cek():
    # print(time.ctime())
    webchecker.webChecker('intent')


schedule.every().hours.at(':01').do(cek)
while True:
    schedule.run_pending()
    time.sleep(1)
