import webchecker
import time
# import webcheckerIntent
import schedule
import time


listWeb = ['intentA', 'intentB', 'intentC', 'intentD',
           'intentE', 'opdA', 'opdB', 'opdC', 'opdD', 'opdE']
listWebTest = ['intentA', 'intentB', 'opdA', 'opdB']

hours = input("Setting Cek Per Jam ? (Integer) ")
print("sistem akan mengecek " + hours + " sekali")


def cek():
    for listW in listWebTest:
        webchecker.webChecker(listW)


cek()

schedule.every(int(hours)).hours.at(':01').do(cek)
while True:
    schedule.run_pending()
    time.sleep(1)
