import urllib.request
import urllib.error
import os
# from tcp_latency import measure_latency


with open('listWeb/test.txt') as file:
    dump = file.read()
    dump = dump.splitlines()


def checkLatency(hostname):
    """
    1. hostname = hostname ex. madiunkota.go.id
    check latency from hostname using os.system for linux -c 
    """
    latency = os.system('ping -c 3 -q -n ' + hostname)
    return latency


for dump in dump:
    try:
        r = urllib.request.urlopen("http://"+dump)
    except Exception as e:
        print(dump + ' ' + str(e))
        print('#'*60)

    if r.getcode() == 200:
        print("\nWebsite " + dump + " NORMAL")
        # checkLatency(dump)
        print('')
        # print(measure_latency(host=url))
        print('#'*60)
    else:
        print("Website " + dump + " Gangguan")
        print("Error Code " + r.getcode() + "\n")
        print('#'*60)
