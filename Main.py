#!/usr/bin/python
import json
from datetime import datetime

from ApiCaller import ApiCaller
from graph import PlotGraph
from Helper import FileIOHelper


uri ='https://s1.ripple.com:51234/'
task = {"method":"server_info","params":[{}]}
filename="test.txt"

#Creating instance
caller = ApiCaller(uri,task)
file = FileIOHelper(filename)
graph = PlotGraph()

#Web Api Calling
resp = caller.requestPost()

if resp.status_code != 200:
    print('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()))

#Parsing Json Data
service_info = json.loads(resp.content.decode('utf-8'))
result = service_info['result'].items()
info = result[0][1]
time = info['time']
ledger = info['validated_ledger']
seq= ledger['seq']
line = str(seq)+" "+(str(time))

#Saving the data in a file
file.FileWrite(line[0:36])

#Reading data from a file and draw graph
data = file.FileRead()
x=[] #time
y=[] #seq
for i in data:
    s = i.split()
    x.append(datetime.strptime(s[2],'%H:%M:%S.%f'))
    y.append(s[0])

graph.setParam(x,y)
graph.showGraph()