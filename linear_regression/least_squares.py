import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches, lines
from canvas.canvas2d import canvas2D


def scatter_values(val):
    arr = np.array([])
    for each in val:
        arr=np.append(arr,np.random.uniform(each-15,each+15))
    return arr

def linear_regression(x_train, y_train):
    # linear regression with gradient descent
    n = 6
    alpha = 0.001
    a_0=0
    a_1=10
    epochs = 0
    while(epochs < 100):
        y = a_0 + a_1 * x_train
        error = y - y_train
        mean_sq_er = np.sum(error**2)
        mean_sq_er = mean_sq_er/n
        # partial derivatives
        a_0 = a_0 - alpha * 2 * np.sum(error)/n 
        a_1 = a_1 - alpha * 2 * np.sum(error * x_train)/n
        epochs += 1
        print("MSE=", round(mean_sq_er,2))
    return a_0, a_1

class LeastSquares(canvas2D):
    canvframes = 95
    def __init__(self, theme='dark'):
        super().__init__(title='', size_xy=(8,80), frames=self.canvframes, xlabel='', atype='l',
                         ylabel='', everyx=1, everyy=10, grid=False, theme=theme, xticklabels=np.arange(0,9), 
                         yticklabels=np.arange(10,90,10))
        # colors for dark bg
        if theme=='dark':
            self.data_color = '#2ACDBB'
            self.funct_color = '#FBEB30'
            self.error_color = '#e50b0b'
        # colors for transparent versions
        elif theme=='light':
            self.data_color = '#3c8c48'
            self.funct_color = '#c43838'
            self.error_color = '#e50b0b'
        # set frames for each animation
        self.scatterframes = 10
        self.lineframes = 10
        self.bflframes = 100
        # configure event to listen to
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        # scattered values
        self.x = np.arange(1,7)
        self.y = np.array([18, 15, 35, 30, 54, 45])
        # self.y = scatter_values(np.arange(10,100,10))
        # wrong line
        self.X = np.arange(1, 8)
        self.Y = np.arange(10, 80, 10)
        # figures
        self.line = lines.Line2D([0], [0], color=self.funct_color)
        self.rect_1 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_2 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_3 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_4 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_5 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        self.rect_6 = patches.Rectangle((0,0), 0, 0, alpha=0.2, color=self.error_color)
        # parameters for best fit line
        self.n = 6
        self.alpha = 0.001
        self.a_0=0
        self.a_1=10

    def animate_scatter(self, i):
        # scatter
        self.ax.scatter(self.x,self.y, s=50, c=None, alpha=.1*i, color=self.data_color, marker='+')
        return self.ax

    def animate_line(self, i):
        self.line.set_data(self.X[:i+1], self.Y[:i+1])
        self.ax.add_line(self.line)
        return self.line,

    def distance_1(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)

        self.ax.text(s=r'{',
                     x=self.X[0]-.45, y=self.Y[0]+1.5, color='white', visible=True,
                     fontsize=55*(1/self.lineframes)*i, alpha=(1/self.lineframes)*i)

        return self.ax,

    def animate_diff_1(self, i):
        if i==0:
            self.ax.add_patch(self.rect_1)
            for txt in self.ax.texts:
                txt.set_visible(False)
        # draw difference
        diff = self.Y[:6]-self.y
        # square distance
        self.rect_1.set_xy((self.x[0], self.y[0]))
        self.rect_1.set_height(diff[0])
        w = (diff[0]/self.lineframes)*i
        self.rect_1.set_width(w/10)
        return self.rect_1,

    def animate_diffs(self, i):
        if i==0:
            self.ax.add_patch(self.rect_2)
            self.ax.add_patch(self.rect_3)
            self.ax.add_patch(self.rect_4)
            self.ax.add_patch(self.rect_5)
            self.ax.add_patch(self.rect_6)
        # draw difference ============
        diff = self.Y[:6]-self.y      
        # square distance
        w = (diff[1]/self.lineframes)*i
        self.rect_2.set_xy((self.x[1], self.y[1]))
        self.rect_2.set_height(diff[1])
        self.rect_2.set_width(w/10)

        w = (diff[2]/self.lineframes)*i
        self.rect_3.set_xy((self.x[2], self.y[2]))
        self.rect_3.set_height(diff[2])
        self.rect_3.set_width(w/10)

        w = (diff[3]/self.lineframes)*i
        self.rect_4.set_xy((self.x[3], self.y[3]))
        self.rect_4.set_height(diff[3])
        self.rect_4.set_width(w/10)
        
        w = (diff[4]/self.lineframes)*i
        self.rect_5.set_xy((self.x[4], self.y[4]))
        self.rect_5.set_height(diff[4])
        self.rect_5.set_width(w/10)

        w = (diff[5]/self.lineframes)*i
        self.rect_6.set_xy((self.x[5], self.y[5]))
        self.rect_6.set_height(diff[5])
        self.rect_6.set_width(w/10)

        return self.rect_2,self.rect_3,self.rect_4,self.rect_5,self.rect_6,self.ax

    def animate_error(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        error = self.Y[:6] - self.y
        error = round(sum(error**2),2)
        self.ax.text(s='Error = {}.00'.format(str(error)), fontproperties=self.prop,
                     x=4, y=10, color=self.error_color,
                     fontsize=50, alpha=(1/self.lineframes)*i)

        return self.ax,

    def animate_best_fit(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        if i>=107:
            i=107
        # calculate best line
        # loop
        pred = self.a_0 + self.a_1 * self.x
        error = pred - self.y
        mean_sq_er = np.sum(error**2)
        # mean_sq_er = mean_sq_er/self.n
        # partial derivatives
        self.a_0 = self.a_0 - self.alpha * 2 * np.sum(error)/self.n 
        self.a_1 = self.a_1 - self.alpha * 2 * np.sum(error * self.x)/self.n
        # move line to best line
        bfy = np.append(pred,(self.a_0 + self.a_1*7))
        self.line.set_data(self.X, bfy)
        self.ax.add_line(self.line)
        # MSE rounded
        MSE = round(mean_sq_er, 2)
        # update error text
        if MSE>350.58:
            self.ax.text(s='Error = {}'.format(str(MSE)), fontproperties=self.prop,
                     x=4, y=10, color=self.error_color,
                     fontsize=50, alpha=1)
        # update rectangles
        self.rect_1.set_height(error[0])
        self.rect_1.set_width(error[0]/10)
        self.rect_2.set_height(error[1])
        self.rect_2.set_width(error[1]/10)
        self.rect_3.set_height(error[2])
        self.rect_3.set_width(error[2]/10)
        self.rect_4.set_height(error[3])
        self.rect_4.set_width(error[3]/10)
        self.rect_5.set_height(error[4])
        self.rect_5.set_width(error[4]/10)
        self.rect_6.set_height(error[5])
        self.rect_6.set_width(error[5]/10)
        if MSE<=350.58:
            # update error text
            self.ax.text(s='Error = 350.58', fontproperties=self.prop,
                         x=4, y=10, color='green',
                         fontsize=50, alpha=1)
            self.rect_1.set_color('green')
            self.rect_2.set_color('green')
            self.rect_3.set_color('green')
            self.rect_4.set_color('green')
            self.rect_5.set_color('green')
            self.rect_6.set_color('green')

        
        return self.ax,self.line

    def animate_predict(self, i):
        y = self.line.get_ydata()[6]
        motion = i/(self.lineframes-1)
        plt.plot([7,7],[0,y*motion], color =self.error_color, linewidth=1.5, linestyle="--", alpha=.5)
        plt.plot([0,7*motion],[y,y], color =self.error_color, linewidth=1.5, linestyle="--", alpha=.5)
        if i>=self.lineframes-1:
            plt.plot([7,7],[y,y], marker='o', markersize=20, markerfacecolor='#ff1e40', markeredgecolor='#ff1e40', alpha=.5)
        return plt,

    def key_press(self, event):
        # Save Image with NO background color
        if event.key == 'I':
            plt.savefig('least_squaresT.png', dpi=None, transparent=True)
        # Save Image with background color
        elif event.key == 'i':
            plt.savefig('canvasB.png', dpi=None, facecolor=self.bg_color)
        # Reset
        elif event.key == '0':
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            self.ax.spines['left'].set_color('none')
            self.ax.spines['bottom'].set_color('none')
        # Separeted animations    
        elif event.key=='1':
            plt.cla()
            plt.xticks(ticks=[], labels='')
            plt.yticks(ticks=[], labels='')
            # self.animate_axes()
            self.static_canvas()
        elif event.key=='2':
            anim = animation.FuncAnimation(self.fig, self.animate_scatter, interval=1, frames=self.scatterframes, blit=False, repeat=False)
        elif event.key=='3':
            anim = animation.FuncAnimation(self.fig, self.animate_line, interval=1, frames=self.lineframes, blit=False, repeat=False)
        elif event.key=='4':
            anim = animation.FuncAnimation(self.fig, self.distance_1, interval=1, frames=self.lineframes, blit=False, repeat=False)
        elif event.key=='5':
            anim = animation.FuncAnimation(self.fig, self.animate_diff_1, interval=1, frames=self.lineframes+1, blit=False, repeat=False)
        elif event.key=='6':
            anim = animation.FuncAnimation(self.fig, self.animate_diffs, interval=1, frames=self.lineframes+1, blit=False, repeat=False)
        elif event.key=='7':
            anim = animation.FuncAnimation(self.fig, self.animate_error, interval=1, frames=self.lineframes+1, blit=False, repeat=False)
        elif event.key=='8':
            anim = animation.FuncAnimation(self.fig, self.animate_best_fit, interval=1, frames=150, blit=False, repeat=False)
            # anim.save('e3.mp4',codec='png', fps=25,
            # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})
        elif event.key=='9':
            anim = animation.FuncAnimation(self.fig, self.animate_predict, interval=1, frames=50, blit=False, repeat=False)
            # anim.save('e4.mp4',codec='png', fps=25,
            # dpi=200, bitrate=100, savefig_kwargs={'facecolor': self.bg_color})
        plt.show()

def main():
    # Hide toolbar from  window
    mpl.rcParams['toolbar'] = 'None'
    # Initiate class
    ls = LeastSquares(theme='dark')
    # Configure position of graph in canvas
    plt.subplots_adjust(left=.3, bottom=.18, right=.73, top=.81, wspace=.20, hspace=.20)
    # showtime
    plt.show()


if __name__ == "__main__":
    main()
