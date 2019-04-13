import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches, lines
from canvas.canvas2d import canvas2D


class ErrorDetail(canvas2D):
    canvframes = 5
    def __init__(self, theme='dark'):
        super().__init__(title='', size_xy=(4,5), frames=self.canvframes, atype='l',
                         everyx=1, everyy=1, grid=False, theme=theme)
        # colors for dark bg
        if theme=='dark':
            self.data_color = '#20ad9d'
            self.funct_color = '#e8dc55'
        # colors for transparent versions
        elif theme=='light':
            self.data_color = '#3c8c48'
            self.funct_color = '#c43838'
        # set frames for each animation
        self.lineframes = 10
        self.bflframes = 100
        # total frames
        self.totalframes = self.canvframes+self.lineframes+self.bflframes
        # configure event to listen to
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        # scattered values
        self.x = np.arange(1,4)
        self.y = np.array([.8, 2.2, 3.5])
        # self.y = scatter_values(np.arange(10,100,10))
        # wrong line
        self.X = np.arange(1, 4)
        self.Y = np.arange(1, 4)
        # figures
        self.line = lines.Line2D([0], [0], color=self.grid_color, linewidth=3)
        self.rect_1 = patches.Rectangle((0,0), 0, 0, alpha=0.4, color='green')
        self.rect_2 = patches.Rectangle((0,0), 0, 0, alpha=0.4, color='green')
        self.rect_3 = patches.Rectangle((0,0), 0, 0, alpha=0.4, color=self.funct_color)
        # parameters for best fit line
        self.n = 6
        self.alpha = 0.001
        self.a_0=0
        self.a_1=10
        self.ang = 0

    def animate_show(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        #points
        self.ax.scatter(self.x,self.y, s=70, c=None, alpha=.1*i, color=self.data_color, marker='+')
        # line
        self.line.set_data(self.X, self.Y)
        self.ax.add_line(self.line)
        # rctangles
        if i==0:
            self.ax.add_patch(self.rect_1)
            self.ax.add_patch(self.rect_2)
            self.ax.add_patch(self.rect_3)
        # draw difference ============
        diff = self.Y-self.y      
        # square distance
        self.rect_1.set_xy((self.x[0], self.y[0]))
        self.rect_1.set_height(diff[0])
        self.rect_1.set_width(diff[0])

        self.rect_2.set_xy((self.x[1], self.y[1]))
        self.rect_2.set_height(diff[1])
        self.rect_2.set_width(diff[1])

        self.rect_3.set_xy((self.x[2], self.y[2]))
        self.rect_3.set_height(diff[2])
        self.rect_3.set_width(diff[2])

        # update error text
        self.ax.text(s='4', fontproperties=self.prop,
                     x=self.x[0]+.05, y=self.y[0], color='green',
                     fontsize=40, alpha=1, va='bottom', ha='left')
        self.ax.text(s='25', fontproperties=self.prop,
                     x=self.x[2], y=self.y[2], color=self.funct_color,
                     fontsize=100, alpha=1,va='top', ha='right')

        return self.line,self.rect_1,self.rect_2,self.rect_3,self.ax

    def animate_fit_line(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)

        d2 = min(self.Y[2] + .003*i, 3.3)
        newy = np.linspace(self.Y[0], d2, 3)
        error = newy - self.y
        self.line.set_data(self.X, newy)
        self.ax.add_line(self.line)
        # fontsize
        fs = 100*(-error[2]/.5)
        # diff
        diff = int((error[2]*10)**2)
        # update error text
        self.ax.text(s='4', fontproperties=self.prop,
                     x=self.x[0]+.05, y=self.y[0], color='green',
                     fontsize=40, alpha=1, va='bottom', ha='left')
        self.ax.text(s=str(diff), fontproperties=self.prop,
                     x=self.x[2], y=self.y[2], color=self.funct_color,
                     fontsize=fs, alpha=1, va='top', ha='right')
        # update rectangles
        self.rect_2.set_height(error[1])
        self.rect_2.set_width(error[1])
        self.rect_3.set_height(error[2])
        self.rect_3.set_width(error[2])

        return self.line,self.rect_1,self.rect_2,self.rect_3,self.ax
        # return self.ax,

    # Animation of whole thing
    def animate(self, i):
        if 0 <= i < self.canvframes:
            _ = self.animate_axis(i)
        if self.canvframes <= i <= self.canvframes+self.lineframes:
            j = i-self.canvframes
            _ = self.animate_show(j)
        if self.canvframes+self.lineframes <= i <= self.canvframes+self.lineframes+self.bflframes:
            k = i - (self.canvframes+self.lineframes)
            _ = self.animate_fit_line(k)
        else:
            i=0
        return self.ax

    def key_press(self, event):
        # Fun full animation and show it
        if event.key == 'a':
            anim = animation.FuncAnimation(self.fig, self.animate, interval=1, frames=self.totalframes, blit=False, repeat=False)
        # Save Video with NO background color
        elif event.key=='V':
            anim = animation.FuncAnimation(self.fig, self.animate, interval=1, frames=self.totalframes, blit=False, repeat=False)
            anim.save('animations/least_squaresT.mp4',codec='png', fps=10, dpi=200, bitrate=10, savefig_kwargs={'transparent': True, 'facecolor': 'none'})
        # Save Video with background color
        elif event.key=='v':
            anim = animation.FuncAnimation(self.fig, self.animate, interval=1, frames=self.totalframes, blit=False, repeat=False)
            anim.save('animations/least_squaresB.mp4',codec='png', fps=10, dpi=200, bitrate=10, savefig_kwargs={'facecolor': self.bg_color})
        if event.key == 'I':
            plt.savefig('images/error_eg.png', dpi=None, transparent=True)
        # Reset
        elif event.key == '0':
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            self.ax.spines['left'].set_color('none')
            self.ax.spines['bottom'].set_color('none')
        # Separeted animations    
        elif event.key=='1':
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            self.animate_axes()
        elif event.key=='2':
            anim = animation.FuncAnimation(self.fig, self.animate_show, interval=1, frames=self.lineframes, blit=False, repeat=False)
        elif event.key=='3':
            anim = animation.FuncAnimation(self.fig, self.animate_fit_line, interval=1, frames=100, blit=False, repeat=False)

        plt.show()

def main():
    # Hide toolbar from  window
    mpl.rcParams['toolbar'] = 'None'
    # Initiate class
    gl = ErrorDetail(theme='light')
    # Configure position of graph in canvas
    plt.subplots_adjust(left=.3, bottom=.18, right=.73, top=.81, wspace=.20, hspace=.20)
    # showtime
    plt.show()


if __name__ == "__main__":
    main()
