import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches, lines
from canvas.canvas2d import canvas2D
from text.text import TextAnim
import matplotlib.patheffects as path_effects


class PartDeriv(canvas2D):
    canvframes = 175
    def __init__(self, theme='dark'):
        super().__init__(size_xy=(120,160), frames=self.canvframes, atype='l',
                         everyx=10, everyy=10, grid=True, theme=theme) # xticklabels=np.arange(-20,90,10), 
                         # yticklabels=np.arange(0,170,10))
        # colors for dark bg
        if theme=='dark':
            self.data_color = '#20ad9d'
            self.funct_color = '#FBEB30'
        # colors for transparent versions
        elif theme=='light':
            self.data_color = '#3c8c48'
            self.funct_color = '#c43838'
        # configure event to listen to
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        # scattered values
        # self.x = np.arange(1,7)-30
        self.x = np.array([-29, -28, -27, -26, -25, -24])
        self.y = np.array([18, 15, 35, 30, 54, 45])
        self.e_values = []
        self.plot_x = []
        self.marker, = plt.plot([0,0],[0,0], marker='o', markersize=20, visible=False,
                    markerfacecolor='w', markeredgecolor='#ff1e40', alpha=1)

    def some_anim(self, i):
        if i>=109:
            i=109
            # self.plot_x.append(i)
            b = np.repeat(i, 6)
            error_b = (self.x + b) - self.y
            error_b = sum(error_b**2)/100
            error_b = round(error_b,2)
            # self.e_values.append(error_b)
            plt.plot(self.plot_x, self.e_values, color='#FCEE16')

        else:
            self.plot_x.append(i)
            b = np.repeat(i, 6)
            error_b = (self.x + b) - self.y
            error_b = sum(error_b**2)/100
            error_b = round(error_b,2)
            self.e_values.append(error_b)
            plt.plot(self.plot_x, self.e_values, color='#FCEE16')

        # print(self.plot_x, self.e_values)

        return plt,

    def animate_some(self, f):
        anim = animation.FuncAnimation(self.fig, self.some_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # anim.save('Regresion/linear_regression/animations/pd1.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        plt.show()

    def change_anim(self, i):
        if i==0:
            self.marker.set_data([self.plot_x[i],self.plot_x[i]],[self.e_values[i],self.e_values[i]])
            self.marker.set_visible(True)
        if i>=99:
            i=99
        self.marker.set_data([self.plot_x[i],self.plot_x[i]],[self.e_values[i],self.e_values[i]])

        if self.plot_x[i]>=56:
            self.ax.fill_between(self.plot_x[56:i], self.e_values[56:i], np.repeat(self.plot_x[0],len(self.plot_x[56:i])),
                                facecolor='#2E742B', alpha=.1, where=self.e_values[56:i]>np.repeat(self.plot_x[0],len(self.plot_x[56:i])))
        elif self.plot_x[i]<56:
            self.ax.fill_between(self.plot_x[:i], self.e_values[:i], np.repeat(self.plot_x[0],i),
                                facecolor='#871724', alpha=.1, where=self.e_values[:i]>np.repeat(self.plot_x[0],i))

        return self.fig,

    def animate_change(self, f):
        anim = animation.FuncAnimation(self.fig, self.change_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # anim.save('Regresion/linear_regression/animations/pd2.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        plt.show()

    def findmin_anim(self, i):
        if self.plot_x[i]>=59:
            self.marker.set_data([self.plot_x[i],self.plot_x[i]],[self.e_values[i],self.e_values[i]])
        # if self.e_values[i]==min(self.e_values):
            # plt.annotate('',xycoords='data', textcoords='data', fontsize=80, 
            #         fontproperties=self.prop, xy=(self.plot_x[i],self.e_values[i]), 
            #         xytext=(self.plot_x[i]-8,self.e_values[i]+40), color='w',
            #         arrowprops=dict(arrowstyle="->", ec='w',fc='w', connectionstyle="arc3,rad=-0.4"))
        # print(self.plot_x[i],self.e_values[i])
        return self.fig,

    def animate_findmin(self, f):
        anim = animation.FuncAnimation(self.fig, self.findmin_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # anim.save('Regresion/linear_regression/animations/pd3.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        plt.show()

    def key_press(self, event):
        if event.key == 'i':
            # Save Image with background
            plt.savefig('Regresion/linear_regression/animations/pd3.png', dpi=None, facecolor=self.bg_color)
        
        # elif event.key == 'I':
        #     # Save Image with NO background
        #     plt.savefig('Regresion/linear_regression/images/pd1.png', dpi=None, transparent=True)
        # reset
        elif event.key == '0':
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            self.ax.spines['left'].set_color('none')
            self.ax.spines['bottom'].set_color('none')

        elif event.key=='1':
            self.static_canvas()
            # self.animate_axes()

        elif event.key=='2':
            self.animate_some(np.arange(10,125,1))
        
        elif event.key=='3':
            self.animate_change(np.arange(0,110))
        
        elif event.key=='4':
            self.animate_findmin(np.arange(99,24,-1))

        plt.show()

def main():
    # Hide toolbar from  window
    mpl.rcParams['toolbar'] = 'None'

    # Initiate class
    ls = PartDeriv(theme='dark')

    # plt.subplots_adjust(left=.3, bottom=.18, right=.73, top=.81, wspace=.20, hspace=.20)
    # Full page
    plt.subplots_adjust(left=0, bottom=0.01, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()