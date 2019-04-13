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
        fpath = os.path.join(rcParams["datapath"], "alterebro_pixel_font/alterebro-pixel-font.ttf")
        self.font = fm.FontProperties(fname=fpath) if font=='pixel' else fm.FontProperties(fname=font)
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
                                **self.alignment, bbox=self.bbox, alpha=1, fontproperties=self.font, 
                                fontsize=self.size, color=self.color, transform=self.ax.transAxes)
        elif self.atype=='increase':
            text = self.ax.text(x=self.x, y=self.y, s=self.text, rotation=self.rot, 
                                **self.alignment, bbox=self.bbox, alpha=(i/(self.frames-1)), 
                                fontproperties=self.font, fontsize=self.size*(i/(self.frames-1)), 
                                color=self.color, transform=self.ax.transAxes)
            # color edges of text
            text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='black'),
                           path_effects.Normal()])
        elif self.atype=='appear':
            text = self.ax.text(x=self.x, y=self.y, s=self.text, rotation=self.rot, 
                                **self.alignment, bbox=self.bbox, alpha=(i/(self.frames-1)), 
                                fontproperties=self.font, fontsize=self.size, 
                                color=self.color, transform=self.ax.transAxes)
            # color edges of text
            text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='black'),
                           path_effects.Normal()])

        return self.ax,

    def show_text(self):
        text = self.ax.text(s=self.text, fontproperties=self.font,
                     x=.5, y=.5, color=self.color, ha='center', va='center',
                     fontsize=self.size)
        if self.annot:
            plt.annotate(self.text, xycoords='data', textcoords='data', fontsize=80, 
                    fontproperties=self.font, xy=(1,.5), xytext=(.7, .8), color=self.color,
                    arrowprops=dict(arrowstyle="->", ec=self.color,fc=self.color, connectionstyle="arc3,rad=-0.4"))
        # color edges of text
        text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='black'),
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

    blue = '#14D8F7'
    yellow = '#FCEE16'
    # equations ================================================================================
    line_eq = r"$pred = \sum_{i=0}^n (m\mathbb{120}+b)$"
    line_eq_ext = r"$pred = (mx_1+b)+(mx_2+b)+(mx_3+b)+...+(mx_n+b)$"
    error_eq = r"$E = \sum_{i=0}^n(pred_i - y_i)^2$"
    error_exp = r"$pred=$ cada valor estimado, $y_i=$cada valor observado"
    dm = r"$\frac{\delta E}{\delta m} = \frac{\sum_{i=0}^n\delta (pred_i - y_i)^2}{\delta m}$"
    
    dm_2 = r"$\sum_{i=0}^n (m x_i^2 + bx_i - x_iy_i) = 0$"
    
    db = r"$\frac{\delta E}{\delta b} = \frac{\sum_{i=0}^n\delta (pred_i - y_i)^2}{\delta b}$"
    
    db_2 = r"$\sum_{i=0}^n (m x_i + b - y_i) = 0$"
    
    m_eq = r"$m=\frac{\sum_{i=0}^nx_iy_i-b\sum_{i=0}^nx_i}{\sum_{i=0}^nx_i^2}$"
    m_eq_2 = r"$m=\frac{\overline{x}\cdot\overline{y}-\overline{xy}}{\overline{x²}-\overline{x}^2}$"
    b_eq = r"$b=\frac{\sum_{i=0}^ny_i-m\sum_{i=0}^nx_i}{n}$"
    b_eq_2 = r"$\overline{y}+m\overline{x}$"

    dedm = r"$\frac{\delta E}{\delta m}$"
    dedb = r"$\frac{\delta E}{\delta b}$"
    m_3 = r"$\frac{\overline{x}\cdot\overline{y}-\overline{xy}}{\overline{x²}-\overline{x}^2}$"

    mediax = r"$\overline{x}=\frac{\sum_{i=0}^nx_i}{n}$"
    #============================================================================================

    T1 = TextAnim(text='Hello', font=None, x=.5, y=.5, rot=0, size=100, 
                color='red', atype='increase', frames=frames, annot=False)

    plt.subplots_adjust(left=.3, bottom=.2, right=.7, top=.8, wspace=.20, hspace=.20)

    T1.show_text()
    # T1.animate_text()

    plt.show()


if __name__ == "__main__":
    main()
