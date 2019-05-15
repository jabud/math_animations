#!/usr/bin/python 
import os
import numpy as np 
import math
import sklearn
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_circles


class HypKernel:
    # config canavas
    def __init__(self, theme):
        # colors for dark bg
        self.bg_color = '#232323'
        self.fig = plt.figure(facecolor=self.bg_color)
        self.ax = Axes3D(self.fig, facecolor=self.bg_color)
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.prop = fm.FontProperties(fname=fpath)
        self.ax.spines['left'].set_color('none')
        self.ax.spines['bottom'].set_color('none')

    def cornersexample(self):
        # Generate example 1 data. 
        n_points = 100
        scale = .2
        loc = 1.
        x_large_yellow = np.random.normal(loc=loc, scale=scale, size=n_points) 
        y_large_yellow = np.random.normal(loc=loc, scale=scale, size=n_points) 
        x_small_yellow = np.random.normal(loc=loc, scale=scale, size=n_points) 
        y_small_yellow = np.random.normal(loc=-loc, scale=scale, size=n_points) 
        x_large_purple = np.random.normal(loc=-loc, scale=scale, size=n_points) 
        y_large_purple = np.random.normal(loc=loc, scale=scale, size=n_points) 
        x_small_purple = np.random.normal(loc=-loc, scale=scale, size=n_points) 
        y_small_purple = np.random.normal(loc=-loc, scale=scale, size=n_points) 
        zmin = -2.
        zmax = 2.

        self.ax.set_xlabel('X', fontproperties=self.prop, fontsize=60, color='w')
        self.ax.set_ylabel('Y', fontproperties=self.prop, fontsize=60, color='w')
        self.ax.set_zlabel('Z', fontproperties=self.prop, fontsize=60, color='r')
        self.ax.set_zticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        self.ax.axis([-2., 2., -2., 2.])
        self.ax.set_zlim([zmin, zmax])

        z_large_yellow = x_large_yellow * y_large_yellow
        z_small_yellow = x_small_yellow * y_small_yellow
        z_large_purple = x_large_purple * y_large_purple
        z_small_purple = x_small_purple * y_small_purple

        self.ax.scatter(x_large_yellow, y_large_yellow, z_large_yellow, c='blue', marker='o', s=60)
        self.ax.scatter(x_small_purple, y_small_purple, z_small_purple, c='blue', marker='o', s=60)
        self.ax.scatter(x_large_purple, y_large_purple, z_large_purple, c='red', marker='x', s=60)
        self.ax.scatter(x_small_yellow, y_small_yellow, z_small_yellow, c='red', marker='x', s=60)

        self.ax.view_init(elev=90,azim=90)

    def hyper_anim(self, i):
        x = np.arange(-2, 2, 0.05)
        y = np.arange(-2, 2, 0.05)
        x, y = np.meshgrid(x, y)
        hyp = x * y
        self.ax.plot_surface(
            x, y, hyp,
            cmap=cm.summer,
            alpha=.01*i,
            linewidth=0,
            antialiased=False,
        )
        return self.ax,plt

    def animate_hyper(self, f):
        anim = animation.FuncAnimation(self.fig, self.hyper_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)

        plt.show()
    
    def plane_anim(self, i):
        # Plot a good planar discriminator.
        x = np.arange(-2, 2, 0.05)
        y = np.arange(-2, 2, 0.05)
        x, y = np.meshgrid(x, y)
        plane = 0. * x
        self.ax.plot_surface(
            x, y, plane,
            alpha=.02*(i),
            linewidth=0,
            antialiased=False,
        )
        return self.ax,plt

    def animate_plane(self, f):
        anim = animation.FuncAnimation(self.fig, self.plane_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)

        plt.show()

    def key_press(self, event):
        # Save Image with NO background color
        if event.key == 'I':
            plt.savefig('img.png', dpi=None, transparent=True)
        # Save Image with background color
        elif event.key == 'i':
            plt.savefig('img_bg.png', dpi=None, facecolor='w')
        # Reset
        elif event.key == '0':
            # some action to reset
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            self.ax.spines['left'].set_color('none')
            self.ax.spines['bottom'].set_color('none')
        # Separeted animations    
        elif event.key=='1':
            # some action
            self.animate_hyper(10)
        elif event.key=='2':
            # some action
            self.animate_plane(10)

        plt.show()


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    svm = HypKernel()
    
    # example
    svm.cornersexample()

    # Configure position of graph in canvas
    plt.subplots_adjust(left=.5, bottom=.2, right=.9, top=.8, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()
