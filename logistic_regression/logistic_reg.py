# Imports
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import font_manager as fm, rcParams, lines
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
from sklearn.datasets import load_breast_cancer


def sigmoid(scores):
    return 1 / (1 + np.exp(-scores))

def sigmoid_line(w,x1, x2):
    return 1 / (1 + np.exp(-w[0]-x1*w[1]-x2*w[2]))


class LogisticRegression:
    def __init__(self):
        self.bg_color = '#232323'
        self.fig_color = '#d8d8d8'
        self.grid_color = '#7c2230'
        self.data_color = '#20ad9d'
        self.funct_color = '#e8dc55'
        #configure canvas
        self.fig = plt.figure(facecolor=self.bg_color)
        self.ax = self.fig.add_subplot(111, aspect='auto', facecolor=self.bg_color)
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.prop = fm.FontProperties(fname=fpath)
        # labels and ticks per axis
        self.ax.xaxis.set_tick_params(color=self.fig_color, labelcolor=self.fig_color)
        self.ax.yaxis.set_tick_params(color=self.fig_color, labelcolor=self.fig_color)
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        # spines position
        self.ax.spines['bottom'].set_position(('data', -0.1))
        self.ax.spines['left'].set_position(('data', -4))
        # axis color
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_color(self.fig_color)
        self.ax.spines['bottom'].set_color(self.fig_color)
       # set linewitdh
        self.ax.spines['left'].set_linewidth(4)
        self.ax.spines['bottom'].set_linewidth(4)
        # ticks
        plt.xticks(ticks=np.arange(-4,9,1), labels=[], size=20)
        plt.yticks(ticks=np.array([0,0.5,1]), labels=np.array([0,0.5,1]), size=20)
        self.ax.set_xlim(-4,8)
        self.ax.set_ylim(-.1,1.1)
        self.ax.tick_params(width=3, length=10, direction='inout')
        # configure event to listen to
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)

        # Prepare data and lines
        np.random.seed(12)
        num_observations = 5000

        x1 = np.random.multivariate_normal([-1, 0], [[1, .75],[.75, 1]], num_observations)
        x2 = np.random.multivariate_normal([2, 4], [[1, .75],[.75, 1]], num_observations)

        self.features = np.vstack((x1, x2)).astype(np.float32)
        self.target = np.hstack((np.zeros(num_observations), np.ones(num_observations)))
        plt.scatter(self.features[:, 1], self.target, alpha = .4)
        # self.features = self.cancer_df["mean perimeter"].values
        # self.target = self.cancer.target
        self.weights = np.zeros(self.features.shape[1])
        self.line = lines.Line2D([0], [0], color=self.funct_color, linewidth=4)

    def log_likelihood(self):
        scores = np.dot(self.features, self.weights)
        ll = np.sum(self.target*scores - np.log(1 + np.exp(scores)))
        return ll

    def logistic_regression(self, i, learning_rate=2.5e-5):
        scores = np.dot(self.features, self.weights)
        predictions = sigmoid(scores)

        # Update weights with gradient
        output_error_signal = self.target - predictions
        gradient = np.dot(self.features.T, output_error_signal)
        self.weights += learning_rate * gradient
        
        # Print log-likelihood every so often
        # if step % 10000 == 0:
            # print(log_likelihood())
        x = np.arange(-4,8,.1)
        y = sigmoid_line(self.weights,x,x)
        self.line.set_data(x,y)
        self.ax.add_line(self.line)

        return self.ax,plt

    def max_likelihood(self, num_steps, add_intercept=True):
        # num_steps = 300000
        # self.weights = self.logistic_regression(simulated_separableish_features, simulated_labels,
        #     learning_rate = 5e-5, add_intercept=True)
        if add_intercept:
            intercept = np.ones((self.features.shape[0], 1))
            self.features = np.hstack((intercept, self.features))
        self.weights = np.zeros(self.features.shape[1])
        anim = animation.FuncAnimation(self.fig, self.logistic_regression, interval=40, 
                                        frames=num_steps, blit=False, repeat=False)

        # matplotlib
        # anim.save('anim_b.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        #moviepy
        # animation = VideoClip(self.line_anim_m, duration=10)
        # animation.write_videofile('anim_b.mp4', fps=25)

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
            self.max_likelihood(num_steps=np.arange(0,60000))

        plt.show()


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    lr = LogisticRegression()

    # Configure position of graph in canvas
    # Centered
    plt.subplots_adjust(left=.35, bottom=.2, right=.75, top=.8, wspace=.20, hspace=.20)
    
    # Full page
    # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()