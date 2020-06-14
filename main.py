import webchecker
import time
# import webcheckerIntent
import schedule
import time

webchecker.webChecker('test')
schedule.every().minutes.do(webchecker.webChecker, 'test')
while True:
    schedule.run_pending()
    time.sleep(1)
