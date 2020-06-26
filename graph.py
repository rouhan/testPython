import matplotlib.pyplot as plt
import numpy as np

class PlotGraph:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def setParam(self):
        plt.plot(self.x, self.y, label='linear')
        # Add a legend
        plt.legend()

    def showGraph(self):
        plt.show()
