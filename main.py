import webchecker
import time
# import webcheckerIntent
import schedule
import time


# print(time.ctime())

listWeb = ['intentA', 'intentB', 'intentC', 'intentD',
           'intentE', 'opdA', 'opdB', 'opdC', 'opdD', 'opdE']
listWebTest = ['intentA', 'intentB', 'opdA', 'opdB']


def cek():
    for listW in listWebTest:
        webchecker.webChecker(listW)


cek()

schedule.every().hours.at(':01').do(cek)
while True:
    schedule.run_pending()
    time.sleep(1)
