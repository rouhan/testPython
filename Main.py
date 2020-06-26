#!/usr/bin/python
import json
from ApiCaller import ApiCaller
from graph import PlotGraph
from Helper import FileIOHelper


uri ='https://s1.ripple.com:51234/'
task = {"method":"server_info","params":[{}]}
filename="test.txt"
#Creating instance
caller = ApiCaller(uri,task)
file = FileIOHelper(filename)

#Web Api Calling
resp = caller.requestPost()

if resp.status_code != 200:
    print('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()))

service_info = json.loads(resp.content.decode('utf-8'))

#Parsing Json Data
result = service_info['result'].items()
info = result[0][1]
time = info['time']
ledger = info['validated_ledger']
seq= ledger['seq']
#Saving the data in a file
file.FileWrite(time)


