import urllib.request
import urllib.error
import os
import datetime
import getFile
# from tcp_latency import measure_latency


def checkLatency(hostname):
    """
    1. hostname = hostname ex. madiunkota.go.id
    check latency from hostname using os.system for linux -c 
    """
    latency = os.system('ping -c 3 -q -n ' + hostname)
    return latency


def webChecker(website):

    link = getFile.getListFile('listWeb/' + website + '.txt')
    print('\n' + format(datetime.datetime.now()) + '\n')
    print('#'*60 + '\n')

    for link in link:
        try:
            r = urllib.request.urlopen("http://"+link)
        except Exception as e:
            """
            Check Error by Code
            """
            print("\nWebsite " + link + " Sedang GANGGUAN \n")
            print(link + ' ' + str(e) + '\n')
            print('#'*60)

        if r.getcode() == 200:
            print("\nWebsite " + link + " NORMAL")
            print("Status 200 HTTP OK")
            # checkLatency(link)
            print('')
            # print(measure_latency(host=url))
            print('#'*60)
        else:
            """
            Check Error by Status Code
            """
            print("\nWebsite " + link + " Sedang GANGGUAN")
            print("Error Code " + format(r.getcode()) + "\n")
            print('#'*60)
