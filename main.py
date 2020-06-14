import webchecker
import time
# import webcheckerIntent
import schedule
import time

webchecker.webChecker()
schedule.every().minutes.do(webchecker.webChecker)
schedule.every().minutes.do(webchecker.webChecker)
while True:
    schedule.run_pending()
    time.sleep(1)
