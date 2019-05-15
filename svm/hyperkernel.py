#!/usr/bin/python 
import os
import numpy as np 
import math
import sklearn
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_circles


class HypKernel:
    # config canavas
    def __init__(self, theme):
        # colors for dark bg
        if theme=='dark':
            self.bg_color = '#232323'
            self.fig_color = '#232323'#d8d8d8
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
        self.fig = plt.figure(facecolor=self.bg_color)
        self.ax = Axes3D(self.fig, facecolor=self.bg_color)
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.prop = fm.FontProperties(fname=fpath)
        # plt.xticks(ticks=[], labels='')
        # plt.yticks(ticks=[], labels='')
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
        # Plot example 1 on a hyperbolic surface.
        x = np.arange(-2, 2, 0.05)
        y = np.arange(-2, 2, 0.05)
        x, y = np.meshgrid(x, y)
        hyp = x * y
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

        # animate
        # self.ax.plot_surface(
        #     x, y, hyp,
        #     cmap=cm.summer,
        #     alpha=.3,
        #     linewidth=0,
        #     antialiased=False,
        # )
        # self.ax.contour(
        #     x, y, hyp,
        #     cmap=cm.summer,
        # )
        # Plot a good planar discriminator.
        # plane = 0. * x
        # self.ax.plot_surface(
        #     x, y, plane,
        #     alpha=.3,
        #     linewidth=0,
        #     antialiased=False,
        # )


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    svm = HypKernel(theme='dark')
    
    svm.cornersexample()

    # Configure position of graph in canvas
    # Centered
    plt.subplots_adjust(left=.5, bottom=.2, right=.9, top=.8, wspace=.20, hspace=.20)
    
    # Full page
    # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()
