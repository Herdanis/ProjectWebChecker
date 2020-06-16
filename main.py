import webchecker
import time
# import webcheckerIntent
import schedule
import time


listWeb = ['intentA', 'intentB', 'intentC', 'intentD',
           'intentE', 'opdA', 'opdB', 'opdC', 'opdD', 'opdE']
listOpd = ['opdA', 'opdB', 'opdC', 'opdD', 'opdE']
listWebTest = ['intentA', 'intentB', 'opdA', 'opdB']

hours = input("Setting Cek Per Jam ? (Integer) ")
print("sistem akan mengecek " + hours + " jam sekali")


def cek(listData, sendId):
    for listW in listData:
        webchecker.webChecker(listW, sendId)


def run():
    cek(listWeb, 1)
    cek(listOpd, 2)


run()

schedule.every(int(hours)).hours.at(':01').do(run)
while True:
    schedule.run_pending()
    time.sleep(1)
