#!/usr/bin/python

import requests
import json

class ApiCaller:

    def __init__(self, url, task):
        self.url = url
        self.task = task

    def requestPost(self):
        resp = requests.post(self.url, json=self.task)
        return resp



