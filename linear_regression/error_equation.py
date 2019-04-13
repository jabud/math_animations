import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches, lines
from canvas.canvas2d import canvas2D
from text.text import TextAnim
import matplotlib.patheffects as path_effects


class ErrorEquation(canvas2D):
    canvframes = 105
    def __init__(self, theme='dark'):
        super().__init__(size_xy=(8,80), frames=self.canvframes, atype='l',
                         everyx=1, everyy=10, grid=False, theme=theme, xticklabels=np.arange(0,9), 
                         yticklabels=np.arange(10,90,10))
        # colors for dark bg
        if theme=='dark':
            self.data_color = '#20ad9d'
            self.funct_color = '#FBEB30'
            self.error_color = '#e50b0b'
        # colors for transparent versions
        elif theme=='light':
            self.data_color = '#3c8c48'
            self.funct_color = '#c43838'
        # configure event to listen to
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        # scattered values
        self.x = np.arange(1,7)
        self.y = np.array([18, 15, 35, 30, 54, 45])
        # wrong line
        self.X = np.arange(1, 8)
        self.Y = np.arange(10, 80, 10)
        # figures
        self.line = lines.Line2D([0], [0], color=self.funct_color)
        self.rect_1 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_2 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_3 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_4 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_5 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_6 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)

    def show_text(self, text):
        text = self.ax.text(s=text, transform=plt.gcf().transFigure,
                     x=.2, y=.85, color='w', ha='center', va='center',
                     fontsize=40)
        # color edges of text
        text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='black'),
                       path_effects.Normal()])

    def last_eg(self):
        # scatter
        self.ax.scatter(self.x,self.y, s=50, alpha=1, color=self.data_color, marker='+')
        self.line.set_data(self.X, self.Y)
        self.ax.add_line(self.line)
        return self.line,

    def distances_anim(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        if i>10:
            i=10
        self.ax.text(s=r'$\{$',
                     x=self.X[0]-.45, y=self.Y[0]+1.5, color='white', visible=True,
                     fontsize=50*i/(10), alpha=i/(10))
        self.ax.text(s=r'$\{$',
                     x=self.X[1]-.3, y=self.Y[1]-5, color='white', visible=True,
                     fontsize=30*i/(10), alpha=i/(10))
        self.ax.text(s=r'$\{$',
                     x=self.X[2]-.3, y=self.Y[2]+1, color='white', visible=True,
                     fontsize=30*i/(10), alpha=i/(10))
        self.ax.text(s=r'{',
                     x=self.X[3]-.5, y=self.Y[3]-8, color='white', visible=True,
                     fontsize=55*i/(10), alpha=i/(10))
        self.ax.text(s=r'{',
                     x=self.X[4]-.2, y=self.Y[4]+1, color='white', visible=True,
                     fontsize=25*i/(10), alpha=i/(10))
        self.ax.text(s=r'{',
                     x=self.X[5]-.8, y=self.Y[5]-13, color='white', visible=True,
                     fontsize=92*i/(10), alpha=i/(10))

        return self.ax,

    def animate_distances(self, f):
        anim = animation.FuncAnimation(self.fig, self.distances_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)
        
        # anim.save('e1.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})
        
        plt.show()

    def diffs_anim(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        if i==0:
            self.ax.add_patch(self.rect_1)
            self.ax.add_patch(self.rect_2)
            self.ax.add_patch(self.rect_3)
            self.ax.add_patch(self.rect_4)
            self.ax.add_patch(self.rect_5)
            self.ax.add_patch(self.rect_6)
        i = int(i/2)
        if i>10:
            i=10
        # draw difference ============
        diff = self.Y[:6]-self.y      
        # square distance
        w = (diff[0]/10)*i
        self.rect_1.set_xy((self.x[0], self.y[0]))
        self.rect_1.set_height(diff[0])
        self.rect_1.set_width(w/10)

        w = (diff[1]/10)*i
        self.rect_2.set_xy((self.x[1], self.y[1]))
        self.rect_2.set_height(diff[1])
        self.rect_2.set_width(w/10)

        w = (diff[2]/10)*i
        self.rect_3.set_xy((self.x[2], self.y[2]))
        self.rect_3.set_height(diff[2])
        self.rect_3.set_width(w/10)

        w = (diff[3]/10)*i
        self.rect_4.set_xy((self.x[3], self.y[3]))
        self.rect_4.set_height(diff[3])
        self.rect_4.set_width(w/10)
        
        w = (diff[4]/10)*i
        self.rect_5.set_xy((self.x[4], self.y[4]))
        self.rect_5.set_height(diff[4])
        self.rect_5.set_width(w/10)

        w = (diff[5]/10)*i
        self.rect_6.set_xy((self.x[5], self.y[5]))
        self.rect_6.set_height(diff[5])
        self.rect_6.set_width(w/10)

        return self.rect_1,self.rect_2,self.rect_3,self.rect_4,self.rect_5,self.rect_6,self.ax

    def animate_diffs(self, f):
        anim = animation.FuncAnimation(self.fig, self.diffs_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)
        
        # anim.save('e2.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})
        
        plt.show()

    def error_anim(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        if i>=10:
            i=10
        error = self.Y[:6] - self.y
        error = round(sum(error**2),2)
        self.ax.text(s='Error = {}.00'.format(str(error)), fontproperties=self.prop,
                     x=4, y=10, color=self.error_color,
                     fontsize=50, alpha=i/10)

        return self.ax,

    def animate_error(self, f):
        anim = animation.FuncAnimation(self.fig, self.error_anim, interval=40, 
                                        frames=None, blit=False, repeat=False)

        # anim.save('e3.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        plt.show()

    def key_press(self, event):
        if event.key == 'i':
            # Save Image with background
            plt.savefig('error_img.png', dpi=None, facecolor=self.bg_color)
        # reset
        elif event.key == '0':
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            self.ax.spines['left'].set_color('none')
            self.ax.spines['bottom'].set_color('none')
        # show x-y axes with x with Ceres values
        elif event.key=='1':
            self.animate_axes()
            # self.static_canvas()
        elif event.key=='2':
            self.last_eg()
        # draw line with x
        elif event.key=='3':
            self.animate_distances(100)
        # move line with m
        elif event.key=='4':
            self.animate_diffs(100)
        # move line with b
        elif event.key=='5':
            self.animate_error(50)

        plt.show()

def main():
    # Hide toolbar from  window
    mpl.rcParams['toolbar'] = 'None'
    # mpl.rc('text', usetext=True)
    # Initiate class
    ls = ErrorEquation(theme='dark')

    # Configure position of graph in canvas
    plt.subplots_adjust(left=.5, bottom=.2, right=.9, top=.8, wspace=.20, hspace=.20)
    # Full page
    # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()
