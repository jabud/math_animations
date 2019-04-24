# Imports
from canvas.canvas2d import canvas2D
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import font_manager as fm, rcParams
from matplotlib import patches
from matplotlib.transforms import Affine2D
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


class TriangleSymm:
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
        # confugure canvas
        self.fig = plt.figure(facecolor=self.bg_color)
        self.ax = self.fig.add_subplot(111, aspect='auto', facecolor=self.bg_color)
        # configure event to listen to
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.prop = fm.FontProperties(fname=fpath)
        # labels and ticks per axis
        self.ax.xaxis.set_tick_params(color=self.bg_color, labelcolor=self.bg_color)
        self.ax.yaxis.set_tick_params(color=self.bg_color, labelcolor=self.bg_color)
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        # axis color
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_color('none')
        self.ax.spines['bottom'].set_color('none')
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        # Triangle
        self.equilateral = patches.RegularPolygon(xy=(0,0), numVertices=3, radius=4, color='#4286f4')
        self.marker1 = patches.RegularPolygon(xy=(-2.6,-1.5), numVertices=20, radius=0.5, color='#59ff77')
        self.marker2 = patches.RegularPolygon(xy=(0,3), numVertices=20, radius=0.5, color='#fff83a')
        self.marker3 = patches.RegularPolygon(xy=(2.6,-1.5), numVertices=20, radius=0.5, color='#ff1e40')

        # Arrays for flips
        # self.p1 = np.array([-4, -2])
        # self.p2 = np.array([0, 4])
        # self.p3 = np.array([4, -2])

    def do_nothing(self, mode, axis='a'):
        if mode=='rot':
            self.ax.add_patch(self.equilateral)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        elif mode=='flip':
            aflip = np.array([[-4, -4], [0, 4], [4, -4]])
            self.equilateral = patches.Polygon(xy=aflip, color='#4286f4')
            self.ax.add_patch(self.equilateral)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
            self.ax.text(s='a', fontproperties=self.prop, x=-0.5, y=4.5, color='w', fontsize=80)
            self.ax.text(s='b', fontproperties=self.prop, x=4.5, y=-4, color='w', fontsize=80)
            self.ax.text(s='c', fontproperties=self.prop, x=-4.5, y=-4, color='w', fontsize=80)
            if axis=='a':
                x = np.zeros(50)
                y = np.linspace(8, -8)
            if axis=='b':
                x = np.linspace(8, -6)
                y = np.linspace(-6.65, 2.7)
            if axis=='c':
                x = np.linspace(-7, 7)
                y = np.linspace(-6, 3.35)
            plt.scatter(x,y, linestyle='--', color='w')
        return self.ax,

    def clock120(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        for txt in self.ax.texts:
            txt.set_visible(False)
        # logic for change by i
        if i>120:
            i=120
        r = Affine2D().rotate_deg_around(0,0, i).inverted() + self.ax.transData
        self.equilateral = patches.RegularPolygon(xy=(0,0), numVertices=3, radius=4, color='#4286f4', transform=r)
        self.marker2 = patches.RegularPolygon(xy=(0,3), numVertices=20, radius=0.5, color='#ff1e40', transform=r)
        self.marker1 = patches.RegularPolygon(xy=(-2.6,-1.5), numVertices=20, radius=0.5, color='#fff83a', transform=r)
        self.marker3 = patches.RegularPolygon(xy=(2.6,-1.5), numVertices=20, radius=0.5, color='#59ff77', transform=r)
        self.ax.add_patch(self.equilateral)
        self.ax.add_patch(self.marker1)
        self.ax.add_patch(self.marker2)
        self.ax.add_patch(self.marker3)
        self.ax.text(s='rot = {}°'.format(str(120-i)), fontproperties=self.prop,
                     x=4, y=4, color='w',
                     fontsize=70)

        return self.ax,

    def anticlock120(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        for txt in self.ax.texts:
            txt.set_visible(False)
        # logic for change by i
        if i>120:
            i=120
        r = Affine2D().rotate_deg_around(0,0, i) + self.ax.transData
        self.equilateral = patches.RegularPolygon(xy=(0,0), numVertices=3, radius=4, color='#4286f4', transform=r)
        self.marker2 = patches.RegularPolygon(xy=(0,3), numVertices=20, radius=0.5, color='#fff83a', transform=r)
        self.marker1 = patches.RegularPolygon(xy=(-2.6,-1.5), numVertices=20, radius=0.5, color='#59ff77', transform=r)
        self.marker3 = patches.RegularPolygon(xy=(2.6,-1.5), numVertices=20, radius=0.5, color='#ff1e40', transform=r)
        self.ax.add_patch(self.equilateral)
        self.ax.add_patch(self.marker1)
        self.ax.add_patch(self.marker2)
        self.ax.add_patch(self.marker3)

        self.ax.text(s='rot = {}°'.format(str(i)), fontproperties=self.prop,
                     x=4, y=4, color='w',
                     fontsize=70)

        return self.ax,

    def clock240(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        for txt in self.ax.texts:
            txt.set_visible(False)
        # logic for change by i
        if i>240:
            i=240
        r = Affine2D().rotate_deg_around(0,0, i).inverted() + self.ax.transData
        self.equilateral = patches.RegularPolygon(xy=(0,0), numVertices=3, radius=4, color='#4286f4', transform=r)
        self.marker2 = patches.RegularPolygon(xy=(0,3), numVertices=20, radius=0.5, color='#59ff77', transform=r)
        self.marker1 = patches.RegularPolygon(xy=(-2.6,-1.5), numVertices=20, radius=0.5, color='#ff1e40', transform=r)
        self.marker3 = patches.RegularPolygon(xy=(2.6,-1.5), numVertices=20, radius=0.5, color='#fff83a', transform=r)
        self.ax.add_patch(self.equilateral)
        self.ax.add_patch(self.marker1)
        self.ax.add_patch(self.marker2)
        self.ax.add_patch(self.marker3)
        self.ax.text(s='rot = {}°'.format(str(240-i)), fontproperties=self.prop,
                     x=4, y=4, color='w',
                     fontsize=70)

        return self.ax,

    def anticlock240(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        for txt in self.ax.texts:
            txt.set_visible(False)
        # logic for change by i
        if i>240:
            i=240
        r = Affine2D().rotate_deg_around(0,0, i) + self.ax.transData
        self.equilateral = patches.RegularPolygon(xy=(0,0), numVertices=3, radius=4, color='#4286f4', transform=r)
        self.marker2 = patches.RegularPolygon(xy=(0,3), numVertices=20, radius=0.5, color='#fff83a', transform=r)
        self.marker1 = patches.RegularPolygon(xy=(-2.6,-1.5), numVertices=20, radius=0.5, color='#59ff77', transform=r)
        self.marker3 = patches.RegularPolygon(xy=(2.6,-1.5), numVertices=20, radius=0.5, color='#ff1e40', transform=r)
        self.ax.add_patch(self.equilateral)
        self.ax.add_patch(self.marker1)
        self.ax.add_patch(self.marker2)
        self.ax.add_patch(self.marker3)
        self.ax.text(s='rot = {}°'.format(str(i)), fontproperties=self.prop,
                     x=4, y=4, color='w',
                     fontsize=70)

        return self.ax,

    def animate_rotate120clock(self, f):
        anim = animation.FuncAnimation(self.fig, self.clock120, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # matplotlib
        # anim.save('rot120.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        plt.show()

    def animate_rotate120anticlock(self, f):
        anim = animation.FuncAnimation(self.fig, self.anticlock120, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # matplotlib
        # anim.save('rot120counter.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        plt.show()

    def animate_rotate240clock(self, f):
        anim = animation.FuncAnimation(self.fig, self.clock240, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # matplotlib
        # anim.save('rot240.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        plt.show()

    def animate_rotate240anticlock(self, f):
        anim = animation.FuncAnimation(self.fig, self.anticlock240, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # matplotlib
        # anim.save('rot240counter.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        plt.show()

    def flip_a(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        if i>10:
            i=10
        
        aflip = np.array([[-4+(i*0.8), -4], [0, 4], [4+(i*(-0.8)), -4]])
        self.equilateral = patches.Polygon(xy=aflip, color='#4286f4')
        self.ax.add_patch(self.equilateral)
        if i==0:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        if i==10:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        return self.ax,

    def flip_a_inverse(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        i = 10 - i
        if i<0:
            i=0
        aflip = np.array([[-4+(i*0.8), -4], [0, 4], [4+(i*(-0.8)), -4]])
        self.equilateral = patches.Polygon(xy=aflip, color='#4286f4')
        self.ax.add_patch(self.equilateral)
        if i==0:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        if i==10:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)

        return self.ax,

    def flip_b(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        if i>10:
            i=10

        aflip = np.array([[-4+(i*0.4), -4+(i*0.8)], [0+(i*-(0.4)), 4+(i*-(0.8))], [4, -4]])
        self.equilateral = patches.Polygon(xy=aflip, color='#4286f4')
        self.ax.add_patch(self.equilateral)
        if i==0:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        if i==10:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)

        return self.ax,

    def flip_b_inverse(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        i = 10 - i
        if i<0:
            i=0

        aflip = np.array([[-4+(i*0.4), -4+(i*0.8)], [0+(i*-(0.4)), 4+(i*-(0.8))], [4, -4]])
        self.equilateral = patches.Polygon(xy=aflip, color='#4286f4')
        self.ax.add_patch(self.equilateral)
        if i==0:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        if i==10:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)

        return self.ax,

    def flip_c(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        if i>10:
            i=10

        aflip = np.array([[-4, -4], [0+(i*0.4), 4+(i*-(0.8))], [4+(i*-(0.4)), -4+(i*0.8)]])
        self.equilateral = patches.Polygon(xy=aflip, color='#4286f4')
        self.ax.add_patch(self.equilateral)
        if i==0:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        if i==10:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        return self.ax,

    def flip_c_inverse(self, i):
        for patch in self.ax.patches:
            patch.set_visible(False)
        i = 10 - i
        if i<0:
            i=0

        aflip = np.array([[-4, -4], [0+(i*0.4), 4+(i*-(0.8))], [4+(i*-(0.4)), -4+(i*0.8)]])
        self.equilateral = patches.Polygon(xy=aflip, color='#4286f4')
        self.ax.add_patch(self.equilateral)
        if i==0:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        if i==10:
            self.marker1 = patches.RegularPolygon(xy=(-2.8,-3.2), numVertices=20, radius=0.65, color='#fff83a', alpha=0.7)
            self.marker2 = patches.RegularPolygon(xy=(0,2.5), numVertices=20, radius=0.65, color='#59ff77', alpha=0.7)
            self.marker3 = patches.RegularPolygon(xy=(2.8,-3.2), numVertices=20, radius=0.65, color='#ff1e40', alpha=0.7)
            self.ax.add_patch(self.marker1)
            self.ax.add_patch(self.marker2)
            self.ax.add_patch(self.marker3)
        return self.ax,

    def animate_flip(self, f, axis='a'):
        if axis=='a':
            anim = animation.FuncAnimation(self.fig, self.flip_a, interval=40, 
                                        frames=f, blit=False, repeat=False)
        if axis=='b':
            anim = animation.FuncAnimation(self.fig, self.flip_b, interval=40, 
                                        frames=f, blit=False, repeat=False)
        if axis=='c':
            anim = animation.FuncAnimation(self.fig, self.flip_c, interval=40, 
                                        frames=f, blit=False, repeat=False)
        # matplotlib
        # anim.save('flip_c.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})
        plt.show()

    def animate_flip_inverse(self, f, axis='a'):
        if axis=='a':
            anim = animation.FuncAnimation(self.fig, self.flip_a_inverse, interval=40, 
                                        frames=f, blit=False, repeat=False)
        if axis=='b':
            anim = animation.FuncAnimation(self.fig, self.flip_b_inverse, interval=40, 
                                        frames=f, blit=False, repeat=False)
        if axis=='c':
            anim = animation.FuncAnimation(self.fig, self.flip_c_inverse, interval=40, 
                                        frames=f, blit=False, repeat=False)
        # matplotlib
        # anim.save('flip_a_inverse.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})
        plt.show()
    
    def key_press(self, event):
        axis='a'
        # Save Image with NO background color
        if event.key == 'I':
            plt.savefig('img.png', dpi=None, transparent=True)
        # Save Image with background color
        elif event.key == 'i':
            plt.savefig('img_bg.png', dpi=None, facecolor='w')
        # Reset
        elif event.key == '0':
            self.do_nothing(mode='rot')
        elif event.key == '9':
            self.do_nothing(mode='flip', axis=axis)
        # Separeted animations    
        elif event.key=='1':
            # some action
            # self.animate_rotate120anticlock(180)
            self.animate_rotate240anticlock(290)
        elif event.key=='2':
            # some action
            # self.animate_rotate120clock(180)
            self.animate_rotate240clock(290)
        elif event.key=='3':
            # some action
            self.animate_flip(65, axis)
        elif event.key=='4':
            # some action
            self.animate_flip_inverse(65, axis)
        plt.show()


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    ts = TriangleSymm(theme='dark')

    # Configure position of graph in canvas
    # Centered
    # plt.subplots_adjust(left=.5, bottom=.2, right=.9, top=.8, wspace=.20, hspace=.20)
    
    # Full page
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()
