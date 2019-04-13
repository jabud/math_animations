import os
from matplotlib import font_manager as fm, rcParams
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import lines
from pandas import read_csv
from sklearn.linear_model import LinearRegression 


class GaltonAnim:
    canvframes = 90
    df = read_csv('linear_regression/galton_data.csv', index_col=0)
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

        plt.title('Regresión Galton', color=self.fig_color, alpha=1, fontproperties=self.prop, fontsize=50)
        plt.xticks(ticks=np.arange(60,81,5), labels=np.arange(60,81,5))
        plt.yticks(ticks=np.arange(60,81,5), labels=np.arange(60,81,5))
        self.ax.set_xlim(60,81)
        self.ax.set_ylim(60,81)
        self.ax.tick_params(width=3, length=10, direction='inout')
        plt.xlabel('padres (in)', color=self.fig_color, fontproperties=self.prop, fontsize=35, 
                            ha='center', va='top', x=.5)
        plt.ylabel('hijos (in)', color=self.fig_color, fontproperties=self.prop, fontsize=35, 
                            ha='right', va='center', y=.5, rotation='vertical')

        # set frames for each animation
        self.scatterframes = 10
        self.lineframes = 10
        self.bflframes = 50
        self.totalframes = self.scatterframes+self.lineframes*2+self.bflframes+10
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        # set values
        x_val = np.array(self.df['CH'].values)
        self.mn = np.mean(x_val)
        self.ind = np.array(self.df['MP'].values)
        self.dep = x_val[:, np.newaxis]
        reg = LinearRegression()
        reg.fit(self.dep, self.ind)
        self.test = np.arange(60,80,.5)
        self.x_test = self.test[:, np.newaxis]
        self.pred = reg.predict(self.x_test)
        self.diff = self.pred-self.test
        self.bfl = lines.Line2D(self.x_test, self.pred, color=self.funct_color)

    def animate_scatter(self, i):
        self.ax.scatter(self.dep,self.ind, s=50, c=None, alpha=.1*i, color=self.data_color, marker='o')
        return self.ax

    def animate_line(self, i):
        plt.plot(np.arange(60,80,.5), np.arange(60,80,.5), color='#c43838', alpha=.1*i)
        # self.ax.add_line(self.line)
        return plt,

    def animate_mean(self, i):
        plt.plot(np.arange(60,80,.5), np.full((40,),self.mn), color='green', alpha=.1*i)
        if i>= self.lineframes-1:
            plt.annotate('Estatura Media',xycoords='data', textcoords='data', fontsize=35, 
                        fontproperties=self.prop, xy=(80, 69), xytext=(80, self.mn), color='g')
        # self.ax.add_line(self.mean)
        return plt,

    def animate_bft(self, i):
        s = self.diff/self.bflframes
        pred_step = self.test+(s*i)
        self.bfl.set_data(self.x_test, pred_step)
        if i>=self.bflframes-1:
            self.bfl.set_data(self.x_test, self.pred)
            plt.annotate('regresa a la media',xycoords='data', textcoords='data', fontsize=35, 
                        fontproperties=self.prop, xy=(self.x_test[-2], self.pred[-2]), xytext=(74, 77.5), color=self.funct_color,
                        arrowprops=dict(arrowstyle="->", ec=self.funct_color,fc=self.funct_color, connectionstyle="arc3,rad=-0.4"))
        self.ax.add_line(self.bfl)
        return self.bfl,

    # Animation of whole thing
    def animate(self, i):
        if 0 <= i < self.scatterframes:
            _ = self.animate_scatter(i)
        if self.scatterframes <= i <= self.scatterframes+self.lineframes:
            j = i-self.scatterframes
            _ = self.animate_mean(j)
        if self.scatterframes+self.lineframes <= i <= self.scatterframes+self.lineframes*2:
            k = i - (self.scatterframes+self.lineframes)
            _ = self.animate_line(k)
        if self.scatterframes+self.lineframes*2 <= i <= self.scatterframes+self.lineframes*2+self.bflframes:
            k = i - (self.scatterframes+self.lineframes*2)
            _ = self.animate_bft(k)

        return self.ax,

    def key_press(self, event):
        # Fun full animation and show it
        if event.key == 'a':
            anim = animation.FuncAnimation(self.fig, self.animate, interval=1, frames=self.totalframes, blit=False, repeat=False)
        elif event.key=='v':
            anim = animation.FuncAnimation(self.fig, self.animate, interval=1, frames=self.totalframes, blit=False, repeat=False)
            anim.save('animations/galton_regB.mp4',codec='png', fps=10, dpi=200, bitrate=10, savefig_kwargs={'facecolor': self.bg_color})
        # Fun full animation and show it
        elif event.key == 'i':
            plt.savefig('images/galton_anim.png', dpi=None, facecolor=self.bg_color)
        if event.key == '0':
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            self.ax.spines['left'].set_color('none')
            self.ax.spines['bottom'].set_color('none')
        # Separeted animations    
        elif event.key=='1':
            anim = animation.FuncAnimation(self.fig, self.animate_scatter, interval=1, frames=self.scatterframes, blit=False, repeat=False)
        elif event.key=='2':
            anim = animation.FuncAnimation(self.fig, self.animate_mean, interval=1, frames=self.lineframes, blit=False, repeat=False)
        elif event.key=='3':
            anim = animation.FuncAnimation(self.fig, self.animate_line, interval=1, frames=self.lineframes, blit=False, repeat=False)
        elif event.key=='4':
            anim = animation.FuncAnimation(self.fig, self.animate_bft, interval=1, frames=self.bflframes, blit=False, repeat=False)

        plt.show()


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'
    # Initiate class
    gl = GaltonAnim(theme='dark')
    # Configure position of graph in canvas
    plt.subplots_adjust(left=.3, bottom=.18, right=.73, top=.81, wspace=.20, hspace=.20)
    # showtime
    plt.show()


if __name__ == "__main__":
    main()
