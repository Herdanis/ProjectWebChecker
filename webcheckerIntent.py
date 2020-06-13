import urllib.request
import urllib.error
import os
# from tcp_latency import measure_latency

with open('listWeb/intent.txt') as file:
    dump = file.read()
    dump = dump.splitlines()


def checkLatency(hostname):
    latency = os.system('ping -c 3 -q -n ' + hostname)
    return latency


for dump in dump:
    try:
        r = urllib.request.urlopen("http://"+dump)
        if r.getcode() == 200:
            print("\nWebsite " + dump + " NORMAL \n ")
            checkLatency(dump)
            print('')
            # print(measure_latency(host=url))
            print('#'*60)
        else:
            print("Website " + dump + " Gangguan")
            print("Error Code " + r.getcode() + "\n")
            print('#'*60)
    except Exception as e:
        print(dump + ' ' + str(e))
        print('#'*60)
