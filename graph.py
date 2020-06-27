from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
FILENAME=""

def animate(i):
    graph_data = open(FILENAME, 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for i in lines:
        s = i.split()
        if len(s) == 0:
            break
        xs.append(datetime.strptime(s[2], '%H:%M:%S.%f'))
        ys.append(s[0])

    ax1.clear()
    ax1.plot(xs, ys)
    plt.xlabel('Time')
    plt.ylabel('Sequence Number')
    plt.gcf().autofmt_xdate()

    # Calculate the min, max, and average time that it took for a new ledger to be validated during the span of time captured.
    # diff = [j - i for i, j in zip(xs[:-1], xs[1:])]
    diff = np.diff(xs)

    minimum = min(diff)
    maximum = max(diff)

    # Converting diff array as datetime array
    sec = []
    for c in diff:
        sec = datetime.strptime(str(c), '%H:%M:%S.%f')

    # Calculating Mean
    mean = (np.array(sec, dtype='datetime64[us]')
            .view('i8')
            .mean()
            .astype('datetime64[us]'))
    x = str(mean).split('T')[1]

    txtstring = '\n'.join((
            "Min Time :"+str(minimum),
            "Max Time :"+str(maximum),
            "Avg Time :"+str(x)))

    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # place a text box in upper left in axes coords
    ax1.text(0.05, 0.95, txtstring, transform=ax1.transAxes, fontsize=8,
            verticalalignment='top' ,bbox=props)


class PlotGraph:

    def __init__(self,filename):
        self.filename = filename

    def setParam(self,x,y):
        # plot
        plt.plot(x, y, label='linear')

        # beautify the x-labels
        plt.gcf().autofmt_xdate()

        # Add a legend
        plt.legend()
        #plt.show()


    def showGraph(self):
        global FILENAME
        FILENAME = self.filename
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
