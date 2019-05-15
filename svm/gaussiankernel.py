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


class GaussianKernel:
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

    def circlesexample(self):
        X,y = make_circles(90, factor=0.2, noise=0.1)
        r = np.exp(-(X**2).sum(1))
        zaxis = [0.2,0.4,0.6,0.8, 1.0]
        zaxislabel = [r'0.2',r'0.4', r'0.6', r'0.8', r'1.0']
        self.ax.scatter(X[:,0], X[:,1], r, c=y, s=70, cmap='seismic')
        self.ax.view_init(elev=90,azim=90)
        self.ax.set_xlabel('X', color='w', fontproperties=self.prop, fontsize=60)
        self.ax.set_ylabel('Y', color='w', fontproperties=self.prop, fontsize=60)
        self.ax.set_zlabel('Z', labelpad=-1, color='red', fontproperties=self.prop, fontsize=60)
        self.ax.set_zticklabels(zaxislabel, fontsize=7, color='none')
        # self.ax.set_zticks([], False)
        self.ax.set_zticks(zaxis)
        plt.xticks(ticks=np.arange(-1.2, 1.4, .2), labels='')
        plt.yticks(ticks=np.arange(-1.2, 1.4, .2), labels='')
        self.ax.grid(linewidth=20)
        return self.fig, 

def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    svm = GaussianKernel(theme='dark')
    
    svm.circlesexample()

    # Configure position of graph in canvas
    # Centered
    plt.subplots_adjust(left=.5, bottom=.2, right=.9, top=.8, wspace=.20, hspace=.20)
    
    # Full page
    # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()
