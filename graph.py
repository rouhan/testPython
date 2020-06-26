import random
import matplotlib.pyplot as plt
import numpy as np
import datetime


class PlotGraph:

    def __init__(self):
        plt.xlabel('Time')
        plt.ylabel('Sequence Number')

    def setParam(self,x,y):
        # plot
        plt.plot(x, y)
        # beautify the x-labels
        plt.gcf().autofmt_xdate()

        #plt.plot(x, y, label='linear')
        # Add a legend
        plt.legend()
        #plt.show()

    def showGraph(self):
        plt.show()
