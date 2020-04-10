import os
import numpy as np 
import sklearn
from matplotlib import font_manager as fm, rcParams
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class LandScape:
    # config canavas
    def __init__(self):
        # colors for dark bg
        self.bg_color = 'black'
        self.fig = plt.figure(facecolor=self.bg_color)
        self.ax = Axes3D(self.fig, facecolor=self.bg_color)
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.prop = fm.FontProperties(fname=fpath)
        # Get rid of colored axes planes
        # First remove fill
        self.ax.xaxis.pane.fill = False
        self.ax.yaxis.pane.fill = False
        self.ax.zaxis.pane.fill = False

        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_color('none')
        self.ax.spines['bottom'].set_color('none')

        # Now set color to white (or whatever is "invisible")
        self.ax.xaxis.pane.set_edgecolor(self.bg_color)
        self.ax.yaxis.pane.set_edgecolor(self.bg_color)
        self.ax.zaxis.pane.set_edgecolor(self.bg_color)

        # Bonus: To get rid of the grid as well:
        self.ax.grid(False)

        self.ax.set_zticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        self.ax.axis([0, 20, 0, 20])
        self.ax.set_zlim([0., 10])

        x = np.arange(0, 100, 1)
        y = np.arange(0, 100, 1)
        self.x, self.y = np.meshgrid(x, y)

    def simple_surface(self):
        surface = np.ones(self.x.shape)
        self.ax.plot_wireframe(
            self.x, self.y, surface,
            color='white'
        )

    def random_surface(self):
        random = np.random.choice(a=[1, 1.2, 1.25, 1.3, 1.35, 1.5, 1.8, 2, 2.2], size=(100,100), 
                                  p=[.7, .05, .05, .025, .025, .05, .05, .025, .025])*np.ones(self.x.shape)
        self.ax.plot_surface(
            self.x, self.y, random,
            color='white'
        )

    def rippled_surface(self):
        # A rippled surface.
        ripple = np.cos((self.x**2 + self.y**2))
        self.ax.plot_wireframe(
            self.x, self.y, ripple,
            color='white'
        )


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    ls = LandScape()
    
    # Surfaces
    # ls.rippled_surface()
    # ls.simple_surface()
    ls.random_surface()

    # Configure position of graph in canvas
    plt.subplots_adjust(left=.5, bottom=.2, right=.9, top=.8, wspace=.20, hspace=.20)
    # plt.subplots_adjust(left=0, bottom=0.01, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()
