import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import font_manager as fm, rcParams, lines
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
from sklearn.datasets import load_breast_cancer
import matplotlib.patheffects as path_effects
import networkx as nx
import random


def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 

    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos


    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


class DecisionTree:
    def __init__(self):
        #configure canvas
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, aspect='auto')
        # axis color
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['left'].set_color('none')
        self.ax.spines['bottom'].set_color('none')

        # axes position
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        # sticks
        plt.yticks([])
        plt.xticks([])
        # configure event to listen to
        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        self.G=nx.Graph()

    def build_tree_1(self, i):
        if i==0:
            plt.cla()
        if i>10:
            i=10
        self.G.add_edges_from([(1,2)])
        pos = hierarchy_pos(self.G, 1)    
        nx.draw(self.G, pos=pos, with_labels=True, alpha=(i/10))

        return self.ax,plt

    def anim_tree_1(self, num_steps):        
        anim = animation.FuncAnimation(self.fig, self.build_tree_1, interval=40, 
                                        frames=num_steps, blit=False, repeat=False)

        # matplotlib
        anim.save('tree1.mp4', codec='png', fps=25,
        dpi=200, bitrate=100, savefig_kwargs={'transparent': True, 'facecolor': 'none'})

        plt.show()

    def build_tree_2(self, i):
        if i==0:
            plt.cla()
        if i>10:
            i=10
        self.G.add_edges_from([(1,2), (1,3)])
        pos = hierarchy_pos(self.G, 1)    
        nx.draw(self.G, pos=pos, with_labels=True, alpha=(i/10))

        return self.ax,plt

    def anim_tree_2(self, num_steps):        
        anim = animation.FuncAnimation(self.fig, self.build_tree_2, interval=40, 
                                        frames=num_steps, blit=False, repeat=False)

        # matplotlib
        anim.save('tree2.mp4', codec='png', fps=25,
        dpi=200, bitrate=100, savefig_kwargs={'transparent': True, 'facecolor': 'none'})

        plt.show()

    def build_tree_3(self, i):
        if i==0:
            plt.cla()
        if i>10:
            i=10
        self.G.add_edges_from([(1,2), (1,3), (2,4), (2,5), (3,6), (3,7)])
        pos = hierarchy_pos(self.G, 1)    
        nx.draw(self.G, pos=pos, with_labels=True, alpha=(i/10))

        return self.ax,plt

    def anim_tree_3(self, num_steps):        
        anim = animation.FuncAnimation(self.fig, self.build_tree_3, interval=40, 
                                        frames=num_steps, blit=False, repeat=False)

        # matplotlib
        anim.save('tree3.mp4', codec='png', fps=25,
        dpi=200, bitrate=100, savefig_kwargs={'transparent': True, 'facecolor': 'none'})

        plt.show()

    def build_tree_4(self, i):
        if i==0:
            plt.cla()
        if i>10:
            i=10
        self.G.add_edges_from([(1,2), (1,3), (2,4), (2,5), (3,6), (3,7),(4,8),(4,9,),(5,10),(5,11),(6,12),(6,13),(7,14),(7,15)])
        pos = hierarchy_pos(self.G, 1)    
        nx.draw(self.G, pos=pos, with_labels=True, alpha=(i/10))

        return self.ax,plt

    def anim_tree_4(self, num_steps):        
        anim = animation.FuncAnimation(self.fig, self.build_tree_4, interval=40, 
                                        frames=num_steps, blit=False, repeat=False)

        # matplotlib
        anim.save('tree4.mp4', codec='png', fps=25,
        dpi=200, bitrate=100, savefig_kwargs={'transparent': True, 'facecolor': 'none'})

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
            self.anim_tree_1(num_steps=50)
        elif event.key=='2':
            self.anim_tree_2(num_steps=50)
        elif event.key=='3':
            # some action
            self.anim_tree_3(num_steps=50)
        elif event.key=='4':
            self.anim_tree_4(num_steps=50)

        plt.show()


def main():
    # Hide toolbar from  window
    rcParams['toolbar'] = 'None'

    # Initiate class
    dt = DecisionTree()

    # Configure position of graph in canvas
    # Centered
    plt.subplots_adjust(left=.35, bottom=.2, right=.75, top=.8, wspace=.20, hspace=.20)
    
    # Full page
    # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=.20, hspace=.20)

    # showtime
    plt.show()


if __name__ == "__main__":
    main()