import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches, lines
from canvas.canvas2d import canvas2D
from text.text import TextAnim
import matplotlib.patheffects as path_effects
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


class LineEquation(canvas2D):
    canvframes = 105
    def __init__(self, theme='dark'):
        super().__init__(size_xy=(80,80), frames=self.canvframes, atype='l',
                         everyy=10, everyx=10, grid=False, theme=theme, xticklabels=np.arange(120,210,10), 
                         )
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
        self.line = lines.Line2D([0], [0], color=self.funct_color)
        self.m = np.array([1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,1.9,1.8,1.7,1.6,1.5,1.4,1.3,1.2,1.1,1,\
                            0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.3,0.4,0.5,0.6,0.7])
        self.b = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,\
                           19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,\
                           -1,-2,-3,-4,-5,-6,-7,-8,-9,-8,-7,-6,-5,-4,-3,-2,-1,0])
        self.x = []
        self.y = []

    def show_text(self, text):
        text = self.ax.text(s=text, transform=plt.gcf().transFigure,
                     x=.2, y=.85, color='w', ha='center', va='center',
                     fontsize=40)
        # color edges of text
        text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='black'),
                       path_effects.Normal()])

        # plt.show()

    def line_anim_x(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        # i=i*8
        if i>80:
            i=80
        eq = 1*i+1
        self.y.append(eq)
        self.x.append(i)
        self.line.set_data(self.x, self.y)
        self.ax.add_line(self.line)

        t = r"$line = \sum_{i=0}^n (m\mathbb{%s}+b)$"%(str(int(i+120)))
        self.show_text(t)
        
        return self.ax,
        # return mplfig_to_npimage(self.fig)
    
    def animate_line_x(self, f):
        anim = animation.FuncAnimation(self.fig, self.line_anim_x, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # matplotlib
        # anim.save('anim_x.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        # moviepy
        # animation = VideoClip(self.line_anim_x, duration=10.5)
        # animation.write_videofile('anim_x.mp4', fps=25)

        plt.show()

    def line_anim_m(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        # i = int(i/.08)
        i = int(i/3)
        if i>33:
            i=33
        self.y = self.m[i]*self.x+1

        self.line.set_data(self.x, self.y)
        self.ax.add_line(self.line)

        t = r"$line = \sum_{i=0}^n (\mathbb{%s}x_i+b)$"%(str(self.m[i]))
        self.show_text(t)

        return self.ax,
        # return mplfig_to_npimage(self.fig)

    def animate_line_m(self, f):
        anim = animation.FuncAnimation(self.fig, self.line_anim_m, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # matplotlib
        # anim.save('anim_m.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        # moviepy
        # animation = VideoClip(self.line_anim_m, duration=3.04)
        # animation.write_videofile('anim_m.mp4', fps=25)

        plt.show()

    def line_anim_b(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        if i>=57:
            i=57
        self.y = 0.7*self.x+self.b[i]

        self.line.set_data(self.x, self.y)
        self.ax.add_line(self.line)

        t = r"$line = \sum_{i=0}^n (mx_i+\mathbb{%s})$"%(str(self.b[i]))
        self.show_text(t)

        return self.ax,
        # return mplfig_to_npimage(self.fig)

    def animate_line_b(self, f):
        anim = animation.FuncAnimation(self.fig, self.line_anim_b, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # matplotlib
        # anim.save('anim_b.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        #moviepy
        # animation = VideoClip(self.line_anim_m, duration=10)
        # animation.write_videofile('anim_b.mp4', fps=25)

        plt.show()

    def key_press(self, event):
        if event.key == 'i':
            # Save Image with background
            plt.savefig('img_bg.png', dpi=None, facecolor=self.bg_color)
        # reset
        elif event.key == '0':
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            self.ax.spines['left'].set_color('none')
            self.ax.spines['bottom'].set_color('none')
        # show x-y axes with x with Ceres values
        elif event.key=='1':
            self.static_canvas()
            # self.animate_axes()
        # draw line with x
        elif event.key=='2':
            self.animate_line_x(np.arange(0,105))
        # move line with m
        elif event.key=='3':
            self.x = np.array(self.x)
            self.y = np.array(self.y)
            self.animate_line_m(np.arange(0,125))
        # move line with b
        elif event.key=='4':
            self.animate_line_b(np.arange(0,100))

        plt.show()

def main():
    # Hide toolbar from  window
    mpl.rcParams['toolbar'] = 'None'
    # mpl.rc('text', usetext=True)
    # Initiate class
    ls = LineEquation(theme='dark')

    # Configure position of graph in canvas
    plt.subplots_adjust(left=.5, bottom=.2, right=.9, top=.8, wspace=.20, hspace=.20)
    # Configuration for Full page
    # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()
