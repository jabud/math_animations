import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from matplotlib import font_manager as fm, rcParams, transforms
import matplotlib.patheffects as path_effects

class TextAnim:
    def __init__(self, text, font, x, y, rot, size, color, atype, frames, annot,
                alignment=None, size_lim=None, bbox=None, fig=None, ax=None):
        self.text = text
        # set custom font
        self.font = font
        fpath1 = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        fpath2 = os.path.join(rcParams["datapath"], "fipps/Fipps-Regular.otf")
        if self.font=='pixel1':
            self.fontprop = fm.FontProperties(fname=fpath1)
        elif self.font=='pixel2':
            self.fontprop = fm.FontProperties(fname=fpath2)
        else: 
            self.fontprop = fm.FontProperties(fname=font)
        self.x = x
        self.y = y
        self.rot = rot
        self.size = size
        self.size_lim = (0, 50)
        self.color = color
        self.alignment = {'horizontalalignment': 'center', 'verticalalignment': 'center'} if not alignment else alignment
        # self.bbox = {'boxstyle': 'round', 'ec': (1.0, 0.5, 0.5), 'fc': (1.0, 0.8, 0.8)}
        self.bbox = bbox
        self.atype = atype
        self.annot = annot
        self.frames = frames
        self.fig = fig
        self.ax = ax
        # canvas config =========================
        if not fig and not ax:
            self.bg_color = '#661436'# '#232323'
            self.fig_color = '#d8d8d8'
            self.grid_color = '#7c2230'
            self.fig = plt.figure(facecolor=self.bg_color)
            self.ax =self.fig.add_subplot(111, facecolor=self.bg_color)
            self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
            # labels and ticks per axis
            # self.ax.xaxis.set_tick_params(color='white', labelcolor='white')
            # self.ax.yaxis.set_tick_params(color='white', labelcolor='white')
            self.fig.patch.set_alpha(0.)
            self.ax.xaxis.set_visible(False)
            self.ax.yaxis.set_visible(False)
            self.ax.set_frame_on(False)
            # axis color
            self.ax.spines['right'].set_color('none')
            self.ax.spines['top'].set_color('none')
            self.ax.spines['left'].set_color('none')
            self.ax.spines['bottom'].set_color('none')

            # axes position
            self.ax.xaxis.set_ticks_position('bottom')
            self.ax.yaxis.set_ticks_position('left')
            # sticks (0 on one axis only)
            plt.yticks([])
            plt.xticks([])
    
    def text_anim(self, i):
        for txt in self.ax.texts:
            txt.set_visible(False)
        
        if self.atype=='typing':
            text = self.ax.text(x=self.x, y=self.y, s=self.text[:i], rotation=self.rot, 
                                **self.alignment, bbox=self.bbox, alpha=1, fontproperties=self.fontprop, 
                                fontsize=self.size, color=self.color, transform=self.ax.transAxes)
        elif self.atype=='increase':
            text = self.ax.text(x=self.x, y=self.y, s=self.text, rotation=self.rot, 
                                **self.alignment, bbox=self.bbox, alpha=(i/(self.frames-1)), 
                                fontproperties=self.fontprop, fontsize=self.size*(i/(self.frames-1)), 
                                color=self.color, transform=self.ax.transAxes)
            # color edges of text
            text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='black'),
                           path_effects.Normal()])
        elif self.atype=='appear':
            text = self.ax.text(x=self.x, y=self.y, s=self.text, rotation=self.rot, 
                                **self.alignment, bbox=self.bbox, alpha=(i/(self.frames-1)), 
                                fontproperties=self.fontprop, fontsize=self.size, 
                                color=self.color, transform=self.ax.transAxes)
        # color edges of text
        if self.font=='pixel1':
            text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='black'),
                       path_effects.Normal()])

        return self.ax,

    def show_text(self):
        text = self.ax.text(s=self.text, fontproperties=self.fontprop,
                     x=.5, y=.5, color=self.color, ha='center', va='center',
                     fontsize=self.size)
        if self.annot:
            plt.annotate(self.text, xycoords='data', textcoords='data', fontsize=80, 
                    fontproperties=self.fontprop, xy=(1,.5), xytext=(.7, .8), color=self.color,
                    arrowprops=dict(arrowstyle="->", ec=self.color,fc=self.color, connectionstyle="arc3,rad=-0.4"))
        # color edges of text
        if self.font=='pixel1':
            text.set_path_effects([path_effects.Stroke(linewidth=20, foreground='black'),
                       path_effects.Normal()])

        plt.show()

    def animate_text(self, save='false'):
        anim = animation.FuncAnimation(self.fig, self.text_anim, interval=1, 
                                    frames=self.frames, blit=False, repeat=False)
        if save=='nobg':
            anim.save('txt_anim.mp4',codec='png', fps=10, 
            dpi=200, bitrate=10, savefig_kwargs={'transparent': True, 'facecolor': 'none'})
            plt.savefig('txt_img.png', dpi=None, transparent=True)
        elif save=='bg':
            anim.save('txt_anim.mp4',codec='png', fps=10,
            dpi=200, bitrate=10, savefig_kwargs={'facecolor': self.bg_color})
        plt.show()

    def key_press(self, event):
        if event.key == 'I':
            # Save Image with NO background
            plt.savefig('txt_img.png', dpi=None, transparent=True)
        elif event.key == 'i':
            # Save Image with background
            plt.savefig('txt_img_bg.png', dpi=None, facecolor=self.bg_color)
        elif event.key == '1':
            # animate
            self.animate_text()
        elif event.key=='V':
            # Save Video with NO background
            self.animate_text(save='nobg')
        elif event.key=='v':
            # Save Video with background
            self.animate_text(save='bg')

        plt.show()

def main():
    rcParams['toolbar'] = 'None'
    frames = 50

    T1 = TextAnim(text='LAB', font='pixel1', x=.5, y=.5, rot=0, size=300, 
                color='w', atype='increase', frames=frames, annot=False)

    plt.subplots_adjust(left=.3, bottom=.2, right=.7, top=.8, wspace=.20, hspace=.20)

    T1.show_text()
    # T1.animate_text()

    plt.show()


if __name__ == "__main__":
    main()
