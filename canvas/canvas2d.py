import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from matplotlib import font_manager as fm, rcParams
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


class canvas2D:
    ''' 
    types: l, t, -, |
    '''
    config = {
        'l':{'position_x':'zero', 'position_y':'zero',
            # Axes labels positions
            'xlabelhor':'center', 'xlabelver':'top', 'x':0.5,
            'ylabelhor':'right', 'ylabelver':'center', 'y':0.5, 'rotation':'vertical'},
        
        't':{'position_x':'center', 'position_y':'center',
            # Axes labels positions
            'xlabelhor':'left', 'xlabelver':'top', 'x':1,
            'ylabelhor':'left', 'ylabelver':'top', 'y':0, 'rotation':'horizontal'},
        # still need testing
        '-':{'position_x':'center', 'position_y':'zero'},
        '|':{'position_x':'zero', 'position_y':('data',20)},
    }
    def __init__(self, title=None, fig=None, ax=None, size_xy=(10,10), frames=10, 
                xlabel=None, ylabel=None, xticklabels='', yticklabels='', transform_type=False, 
                everyx=1, everyy=1, grid=False, theme='dark', atype='l', atype2=None):
        if transform_type and not atype2:
            raise ValueError("atype2 config is required")
        self.atype = atype
        self.atype2 = atype2
        self.title = title
        if theme=='dark':
            self.bg_color = '#232323'
            self.fig_color = '#d8d8d8'
            self.grid_color = '#14D8F7' #'#7c2230'
        elif theme=='light':
            self.bg_color = '#e2deb3'
            self.fig_color = '#232323'
            self.grid_color = '#46abea'
        self.size_xy = size_xy
        self.frames = frames
        self.everyx = everyx
        self.everyy = everyy
        self.grid = grid
        self.countx = 0
        self.county = 0
        self.ylabel = ylabel
        self.xlabel = xlabel
        self.xticklabels = xticklabels
        self.yticklabels = yticklabels
        self.fig = plt.figure(facecolor=self.bg_color) if not fig else fig
        self.ax = self.fig.add_subplot(111, facecolor=self.bg_color) if not ax else ax

        # set custom font
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.prop = fm.FontProperties(fname=fpath)

        # labels and ticks per axis
        self.ax.xaxis.set_tick_params(color=self.fig_color, labelcolor=self.fig_color)
        self.ax.yaxis.set_tick_params(color=self.fig_color, labelcolor=self.fig_color)

        # axis color
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_color('none')
        self.ax.spines['bottom'].set_color('none')

        # axes position
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        # sticks
        plt.yticks([])
        plt.xticks([])

    def set_motion(self, i, tot, count):
        if self.frames>tot:
            steps = int(self.frames/tot)
            if not i%steps:
                count += 1
        elif self.frames<tot:
            steps = round(tot/self.frames)
            count = min(i*steps, tot)
        else:
            count = i
        return count

    def axes_anim(self,i):
        # i = int(i/2)
        if i == 0:
            return self.ax,plt
            # return mplfig_to_npimage(self.fig)
        if self.title:
            plt.title(self.title, color=self.fig_color, alpha=i/(self.frames-1), fontproperties=self.prop, fontsize=50*i/(self.frames-1))
        # set axes by type of canvas
        # spines position
        self.ax.spines['bottom'].set_position(self.config[self.atype]['position_x'])
        self.ax.spines['left'].set_position(self.config[self.atype]['position_y'])
        # colors
        self.ax.spines['left'].set_color(self.fig_color)
        self.ax.spines['bottom'].set_color(self.fig_color)
        # set linewitdh
        self.ax.spines['left'].set_linewidth(3)
        self.ax.spines['bottom'].set_linewidth(3)

        self.countx = min(i, self.size_xy[0])
        self.county = min(i, self.size_xy[1])
        plt.xticks(ticks=np.arange(0,self.countx+self.everyx,self.everyx), labels=self.xticklabels, size=25)
        y_start = self.everyy if self.atype=='l' else 0
        plt.yticks(ticks=np.arange(y_start,self.county+self.everyy,self.everyy), labels=self.yticklabels, size=25)
        
        self.ax.set_xlim(0,self.countx)
        self.ax.set_ylim(0,self.county)
        # grid
        if self.grid:
            plt.grid(b=True, which='major', axis='both', color=self.grid_color, linestyle='-', linewidth=.6, alpha=.6)
            self.ax.tick_params(length=0)
        elif not self.grid:
            self.ax.tick_params(width=2, length=10, direction='inout')
        if i>=self.frames-1:
            self.countx=0
            self.county=0
            # set labels
            if self.xlabel:
                plt.xlabel(self.xlabel, color=self.fig_color, fontproperties=self.prop, fontsize=35, 
                            horizontalalignment=self.config[self.atype]['xlabelhor'], 
                            verticalalignment=self.config[self.atype]['xlabelver'], x=self.config[self.atype]['x'])
            if self.ylabel:
                plt.ylabel(self.ylabel, color=self.fig_color, fontproperties=self.prop, fontsize=35, 
                            horizontalalignment=self.config[self.atype]['ylabelhor'], rotation=self.config[self.atype]['rotation'],
                            verticalalignment=self.config[self.atype]['ylabelver'], y=self.config[self.atype]['y'])

        return self.ax,
        # return mplfig_to_npimage(self.fig)


    def switch_canvas_anim(self, i):
        if i==0:
            # colors
            self.ax.spines['left'].set_color(self.fig_color)
            self.ax.spines['bottom'].set_color(self.fig_color)
            # set linewitdh
            self.ax.spines['left'].set_linewidth(2)
            self.ax.spines['bottom'].set_linewidth(2)
            # set axes by type of canvas
        if self.atype=='l':
            transition = np.linspace(0, 0.5, self.frames)
        elif self.atype=='t':
            transition = np.linspace(0.5, 0, self.frames)
        
        # spines position
        self.ax.spines['bottom'].set_position(('axes', transition[i]))
        self.ax.spines['left'].set_position(('axes', transition[i]))
        self.ax.set_xlim(0, self.atype2['size_xy'][0])
        self.ax.set_ylim(0, self.atype2['size_xy'][1])
        # deal with ntlabels
        plt.yticks([])
        plt.xticks([])
        if i==self.frames-1:
            self.ax.set_xlim(0, self.atype2['size_xy'][0])
            self.ax.set_ylim(0, self.atype2['size_xy'][1])
            plt.xticks(ticks=np.arange(0, self.atype2['size_xy'][0]+1,self.atype2['everyx']), labels=self.atype2['xtlabels'])
            y_start = self.everyy if self.atype2['atype']=='l' else 0
            plt.yticks(ticks=np.arange(y_start,self.atype2['size_xy'][1]+1, self.atype2['everyy']), labels=self.atype2['ytlabels'])

        return self.ax,plt

    def static_canvas(self):
        if self.title:
            plt.title(self.title, color=self.fig_color, alpha=1, fontproperties=self.prop, fontsize=50)
        
        # spines position
        self.ax.spines['bottom'].set_position(self.config[self.atype]['position_x'])
        self.ax.spines['left'].set_position(self.config[self.atype]['position_y'])

        # colors
        self.ax.spines['left'].set_color(self.fig_color)
        self.ax.spines['bottom'].set_color(self.fig_color)
        # set linewitdh
        self.ax.spines['left'].set_linewidth(3)
        self.ax.spines['bottom'].set_linewidth(3)

        plt.xticks(ticks=np.arange(0,self.size_xy[0]+self.everyx,self.everyx), labels=self.xticklabels, size=25)
        y_start = self.everyy if self.atype=='l' else 0
        plt.yticks(ticks=np.arange(y_start,self.size_xy[1]+self.everyy,self.everyy), labels=self.yticklabels, size=25)
        
        self.ax.set_xlim(0,self.size_xy[0])
        self.ax.set_ylim(0,self.size_xy[1])
        # grid
        if self.grid:
            plt.grid(b=True, which='major', axis='both', color=self.grid_color, linestyle='-', linewidth=.6, alpha=.6)
            self.ax.tick_params(length=0)
        elif not self.grid:
            self.ax.tick_params(width=2, length=10, direction='inout')
        # set labels
        if self.xlabel:
            plt.xlabel(self.xlabel, color=self.fig_color, fontproperties=self.prop, fontsize=35, 
                        horizontalalignment=self.config[self.atype]['xlabelhor'], 
                        verticalalignment=self.config[self.atype]['xlabelver'], x=self.config[self.atype]['x'])
        if self.ylabel:
            plt.ylabel(self.ylabel, color=self.fig_color, fontproperties=self.prop, fontsize=35, 
                        horizontalalignment=self.config[self.atype]['ylabelhor'], rotation=self.config[self.atype]['rotation'],
                        verticalalignment=self.config[self.atype]['ylabelver'], y=self.config[self.atype]['y'])

        return self.fig

    def animate_axes(self):
        anim = animation.FuncAnimation(self.fig, self.axes_anim, interval=40, 
                                frames=self.frames, blit=False, repeat=False)

        # anim.save('Regresion/linear_regression/animations/pd0.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})
        
        # animation = VideoClip(self.axes_anim, duration=4.2)
        # animation.write_videofile('Regresion/linear_regression/animations/1.mp4', fps=25)
        plt.show()

    def switch_type(self):
        anim = animation.FuncAnimation(self.fig, self.switch_canvas_anim, interval=10, 
                                    frames=self.frames, blit=False, repeat=False)
        plt.show()


def main():
    frames = 21
    trans = {
        'atype':'l', 'size_xy':(10,10), 'xtlabels':np.arange(0,11), 'ytlabels':np.arange(0,11),
        'everyx':1, 'everyy':1,
        }
    cvs = canvas2D(size_xy=(20,20), frames=frames, atype='l', transform_type=True, atype2=trans,
                    xticklabels=np.arange(-10,11), yticklabels=np.arange(-10,11), grid=False, theme='dark')
    cvs.animate_axes()


if __name__ == "__main__":
    main()
