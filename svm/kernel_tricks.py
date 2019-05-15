import os
import numpy as np 
import sklearn
from matplotlib import font_manager as fm, rcParams
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class KernelExamples:
    # config canavas
    def __init__(self, theme):
        # colors for dark bg
        self.bg_color = '#232323'
        self.fig = plt.figure(facecolor=self.bg_color)
        self.ax = Axes3D(self.fig, facecolor=self.bg_color)
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.prop = fm.FontProperties(fname=fpath)
        self.ax.spines['left'].set_color('none')
        self.ax.spines['bottom'].set_color('none')
        x = np.arange(-2, 2, 0.05)
        y = np.arange(-2, 2, 0.05)
        self.x, self.y = np.meshgrid(x, y)


    def quadratic_surface(self):
        quadratic = self.x**2 * self.y**2
        self.ax.plot_surface(
            self.x, self.y, quadratic,
            cmap=cm.summer,
            alpha=.3,
            linewidth=0,
            antialiased=False,
        )
        self.ax.contour(self.x, self.y, quadratic, cmap=cm.summer)
        self.ax.set_zticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        self.ax.axis([-2., 2., -2., 2.])
        self.ax.set_zlim([0, 4.])

    def rippled_surface(self):
        # A rippled surface.
        ripple = np.cos((self.x**2 + self.y**2)**.5)**2
        self.ax.plot_surface(
            self.x, self.y, ripple,
            cmap=cm.summer,
            alpha=.3,
            linewidth=0,
            antialiased=False,
        )
        self.ax.contour(self.x, self.y, ripple, cmap=cm.summer)
        self.ax.set_zticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        self.ax.axis([-2., 2., -2., 2.])
        self.ax.set_zlim([0., 1.])

    def peaked_surface(self):
        peaked = np.cos(2 * self.x) * np.sin(3 * self.y)
        self.ax.plot_surface(
            self.x, self.y, peaked,
            cmap=cm.summer,
            alpha=.3,
            linewidth=0,
            antialiased=False,
        )
        self.ax.contour(self.x, self.y, peaked, cmap=cm.summer)
        self.ax.set_zticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        self.ax.axis([-2., 2., -2., 2.])
        self.ax.set_zlim([-1., 1.])

    def quadratic_surface2(self):
        # Optionally, show the resulting quadratic surface.
        show_surface = True
        shift = 2.2
        if show_surface:
            dual_quad = self.y**2 - shift
            self.ax.plot_surface(
                self.x, self.y, dual_quad,
                cmap=cm.summer,
                alpha=.3,
                linewidth=0,
                antialiased=False,
            )

        # Optionally, show a good planar discriminator.
        show_discriminator = False
        if show_discriminator:
            plane = 0. * self.x
            self.ax.plot_surface(
                self.x, self.y, plane,
                alpha=.3,
                linewidth=0,
                antialiased=False,
            )
        self.ax.set_xlabel('')
        self.ax.set_zticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_xticklabels([])
        self.ax.axis([-3., 3., -3., 3.])
        self.ax.set_zlim([-4., 4.])


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    svm = KernelExamples()
    
    # Surfaces
    # svm.quadratic_surface()
    svm.quadratic_surface2()
    # svm.rippled_surface()
    # svm.peaked_surface()

    # Configure position of graph in canvas
    plt.subplots_adjust(left=.5, bottom=.2, right=.9, top=.8, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()
