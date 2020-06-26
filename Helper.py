#!/usr/bin/python
class FileIOHelper:

    def __init__(self, filename):
        self.filename = filename

    def FileWrite(self,text):
        # f = open(self.filename, "w+")
        f=open(self.filename,"a+")
        f.write(text)
        f.write("\n")
        f.close()


    def FileRead(self,text):
        f = open(self.filename, "r")
        f1=f.readlines()
        f.close()
        return f1