import random
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

from matplotlib.figure import Figure

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open('test.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    sec = []
    for i in lines:
        s = i.split()
        if len(s) == 0:
            break
        xs.append(datetime.strptime(s[2], '%H:%M:%S.%f'))
        ys.append(s[0])

    diff =[j-i for i, j in zip(xs[:-1], xs[1:])]
    #diff = np.diff(xs)
    minimum = min(diff)
    maximum = max(diff)

    # total = np.add(diff)
    # #total =  sum(diff)
    # length = len(diff)
    # average = sum / length
    ax1.clear()
    ax1.plot(xs, ys)
    plt.xlabel('Time')
    plt.ylabel('Sequence Number')
    plt.gcf().autofmt_xdate()
    #Calculate the min, max, and average time that it took for a new ledger to be validated during the span of time captured.


class PlotGraph:

    def __init__(self):
        print()

    def setParam(self,x,y):
        # plot
        plt.plot(x, y, label='linear')

        # beautify the x-labels
        plt.gcf().autofmt_xdate()

        #plt.plot(x, y, label='linear')
        # Add a legend
        plt.legend()
        #plt.show()

    def showGraph(self):
        ani =  animation.FuncAnimation(fig,animate,interval=1000)
        plt.show()
