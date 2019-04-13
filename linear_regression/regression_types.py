import os
from matplotlib import font_manager as fm, rcParams
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 


def scatter_values(val, n):
    arr = np.array([])
    for each in val:
        arr=np.append(arr,np.random.uniform(each-1.5,each+1.5, n))
    return arr

def sigmoid(x):
    return (8/(1 + np.exp(-x)))+1

class regressionTypes:
    def __init__(self, theme):
        # colors for dark bg
        if theme=='dark':
            self.bg_color = '#232323'
            self.fig_color = '#d8d8d8'
            self.grid_color = '#7c2230'
            self.data_color = '#20ad9d'
            self.funct_color = '#e8dc55'
        # colors for transparent versions
        elif theme=='light':
            self.bg_color = '#e2deb3'
            self.fig_color = '#232323'
            self.grid_color = '#46abea'
            self.data_color = '#3c8c48'
            self.funct_color = '#c43838'
        #configure canvas
        self.fig = plt.figure(facecolor=self.bg_color)
        self.ax = self.fig.add_subplot(111, aspect='auto', facecolor=self.bg_color)
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.prop = fm.FontProperties(fname=fpath)
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        # labels and ticks per axis
        self.ax.xaxis.set_tick_params(color=self.fig_color, labelcolor=self.fig_color)
        self.ax.yaxis.set_tick_params(color=self.fig_color, labelcolor=self.fig_color)
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        # # spines position
        # self.ax.spines['bottom'].set_position('zero')
        # self.ax.spines['left'].set_position('zero')
        # axis color
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_color(self.fig_color)
        self.ax.spines['bottom'].set_color(self.fig_color)
       # set linewitdh
        self.ax.spines['left'].set_linewidth(3)
        self.ax.spines['bottom'].set_linewidth(3)

        plt.title('', color=self.fig_color, alpha=1, fontproperties=self.prop, fontsize=50)
        plt.xticks([])
        plt.yticks([])
        self.ax.set_xlim(0,11)
        self.ax.set_ylim(0,11)
        # self.ax.tick_params(width=3, length=10, direction='inout')
    
    def nolineal(self):
        line = []
        for x in np.arange(0,10, .1): 
            val = 3*np.sin(x)+2*np.cos(x)+5
            line.append(val)
        data = scatter_values(line, 5)
        # x axes
        line_x = np.arange(0, 10, .1)
        data_x = np.repeat(line_x, 5)
        plt.scatter(data_x, data, color=self.data_color)
        plt.plot(line_x, line, color=self.funct_color, linewidth=3)
        plt.show()

    def logistica(self):
        line = []
        for x in np.arange(-10,10, .1): 
            val = sigmoid(x)
            line.append(val)
        data1 = scatter_values(np.repeat(1,100), 4)
        data2 = scatter_values(np.repeat(1,100), 1)
        data3 = scatter_values(np.repeat(9,100), 1)
        data4 = scatter_values(np.repeat(9,100), 4)
        # x axes
        line_x = np.arange(0, 10, .05)
        data_x1 = np.repeat(line_x, 4)
        data_x2 = np.repeat(line_x, 1)


        plt.scatter(data_x1[:400], data1, color=self.data_color)
        plt.scatter(data_x2[100:], data2, color=self.data_color)
        plt.scatter(data_x2[:100], data3, color=self.data_color)
        plt.scatter(data_x1[400:], data4, color=self.data_color)

        plt.plot(line_x, line, color=self.funct_color, linewidth=3)
        plt.show()

    def bayesiana(self):
        mu, sigma = 1.5, .2
        s = np.random.normal(mu, sigma, 1000)
        count, bins, ignored = plt.hist(s, 30, normed=True, visible=False)
        plt.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2)),
                linewidth=3, color=self.funct_color)
        plt.plot([1.5,1.5], [0,2], linewidth=3, color=self.data_color, linestyle="--")
        plt.show()

    def etc(self):
        self.ax.text(s='etc..', fontproperties=self.prop,
                     x=4.5, y=5, color=self.data_color,
                     fontsize=100)
        plt.show()

    def key_press(self, event):
        if event.key == 'I':
            plt.savefig('logistic.png', dpi=None, transparent=True)
        # Save Image with background color
        elif event.key == 'i':
            plt.savefig('logistic_bg.png', dpi=None, facecolor=self.bg_color)


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'
    # Initiate class
    rt = regressionTypes(theme='light')
    # Configure position of graph in canvas
    plt.subplots_adjust(left=.3, bottom=.18, right=.73, top=.81, wspace=.20, hspace=.20)
    rt.logistica()
    # showtime
    # plt.show()


if __name__ == "__main__":
    main()