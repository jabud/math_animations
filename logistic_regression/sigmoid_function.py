# Imports
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import font_manager as fm, rcParams
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
from sklearn.datasets import load_breast_cancer



def sigmoid(scores):
    return 1 / (1 + np.exp(-scores))

def log_likelihood(features, target, weights):
    scores = np.dot(features, weights)
    ll = np.sum( target*scores - np.log(1 + np.exp(scores)) )
    return ll

def logistic_regression(features, target, num_steps, learning_rate, add_intercept = False):
    if add_intercept:
        intercept = np.ones((features.shape[0], 1))
        features = np.hstack((intercept, features))
        
    weights = np.zeros(features.shape[1])
    
    for step in xrange(num_steps):
        scores = np.dot(features, weights)
        predictions = sigmoid(scores)

        # Update weights with gradient
        output_error_signal = target - predictions
        gradient = np.dot(features.T, output_error_signal)
        weights += learning_rate * gradient
        
        # Print log-likelihood every so often
        if step % 10000 == 0:
            print log_likelihood(features, target, weights)
        
    return weights

# weights = logistic_regression(simulated_separableish_features, simulated_labels,num_steps = 300000, learning_rate = 5e-5, add_intercept=True)


class Sigmoid:
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
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.spines['left'].set_position(('data', -10))
        # axis color
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_color(self.fig_color)
        self.ax.spines['bottom'].set_color(self.fig_color)
       # set linewitdh
        self.ax.spines['left'].set_linewidth(2)
        self.ax.spines['bottom'].set_linewidth(2)
        # ticks
        plt.xticks(ticks=np.arange(-10,11,1), labels=np.arange(-10,11,1), size=20)
        plt.yticks(ticks=np.array([0,0.5,1]), labels=np.array([0,0.5,1]), size=20)
        self.ax.set_xlim(-10,10)
        self.ax.set_ylim(0,1)
        self.ax.tick_params(width=3, length=10, direction='inout')
        # configure event to listen to
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        self.cancer = load_breast_cancer()
        self.cancer_df=pd.DataFrame(self.cancer.data,columns=cancer.feature_names)
        self.x = np.arange(-10,10)
        self.y = self.cancer.target

    def m_anim(self, i):
        # logic for change by i
        b=0
        m=1*(i/59)
        sig = 1/(1 + np.exp(-b-m*self.x))
        plt.plot(self.x, sig, color='b')
        return self.ax,plt
        # return mplfig_to_npimage(self.fig)

    def animate_m(self, f):
        anim = animation.FuncAnimation(self.fig, self.m_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)

        # matplotlib
        # anim.save('anim_b.mp4',codec='png', fps=25,
        # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})

        #moviepy
        # animation = VideoClip(self.line_anim_m, duration=10)
        # animation.write_videofile('anim_b.mp4', fps=25)

        plt.show()

    def b_anim(self, i):
        # logic for change by i
        b=5*(i/59)
        m=1
        sig = 1/(1 + np.exp(-b-m*self.x))
        plt.plot(self.x, sig, color='b')
        return self.ax,plt
        # return mplfig_to_npimage(self.fig)

    def animate_b(self, f):
        anim = animation.FuncAnimation(self.fig, self.b_anim, interval=40, 
                                        frames=f, blit=False, repeat=False)

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
            self.animate_m(np.arange(0,60))
        elif event.key=='2':
            # some action
            self.animate_b(np.arange(-60,60))
        plt.show()


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    sig = Sigmoid()

    # Configure position of graph in canvas
    # Centered
    plt.subplots_adjust(left=.3, bottom=.2, right=.7, top=.8, wspace=.20, hspace=.20)
    
    # Full page
    # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()