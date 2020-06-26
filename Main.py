#!/usr/bin/python
import json
import datetime
import logging
import threading
import time

from ApiCaller import ApiCaller
from graph import PlotGraph
from Helper import FileIOHelper


WAIT_SECONDS = 2
URI ='https://s1.ripple.com:51234/'
TASK = {"method":"server_info","params":[{}]}
FILE_NAME="test.txt"

#Creating instance
caller = ApiCaller(URI,TASK)
file = FileIOHelper(FILE_NAME)
graph = PlotGraph()
threads = list()

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

#Web Api Calling Function
def thread_function(number):
    while True:
        resp = caller.requestPost()

        if resp.status_code != 200:
            print('POST /tasks/ {}'.format(resp.status_code))
        print('Created task. ID: {}'.format(resp.json()))

        #Parsing Json Data
        service_info = json.loads(resp.content.decode('utf-8'))
        result = service_info['result'].items()
        info = result[0][1]
        times = info['time']
        ledger = info['validated_ledger']
        seq= ledger['seq']
        line = str(seq)+" "+(str(times))

        #Saving the data in a file
        file.FileWrite(line[0:36])
        time.sleep(WAIT_SECONDS)

#Opening thread for calling Web API
x = threading.Thread(target=thread_function, args=(1,))
threads.append(x)
x.start()

#Opening thread for Graph
y = threading.Thread(target=graph.showGraph(), args=(2,))
threads.append(y)
y.start()

for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)




#Reading data from a file and draw graph
# data = file.FileRead()
# x=[] #time
# y=[] #seq
# for i in data:
#     s = i.split()
#     x.append(datetime.strptime(s[2],'%H:%M:%S.%f'))
#     y.append(s[0])
#
# graph.setParam(x,y)
# Show Graph
#graph.showGraph()