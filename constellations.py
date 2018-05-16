'''
Created on May 16, 2018

@author: vedecom
'''

import matplotlib 
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('bmh')
plt.rcParams['figure.facecolor'] = '#222222'
plt.rcParams['axes.facecolor'] = 'None'
plt.rcParams['figure.figsize'] = (10, 10.0*2/3)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = '3'
plt.rcParams['text.color'] = 'white'

import ieee802_11

def const_plot():
    plt.axis('off')
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.arrow(-1.2, 0, 2.4, 0, head_width=0.05, head_length=0.1, fc='gray', ec='gray')
    plt.arrow(0, -1.2, 0, 2.4, head_width=0.05, head_length=0.1, fc='gray', ec='gray')
    plt.xlim(-1.4, 1.4)
    plt.ylim(-1.5, 1.5)

###############################################
#                 16-QAM
###############################################

c = ieee802_11.constellation_16qam()
a = np.array(c.points())
p = np.average(np.abs(a)**2)
level = .1**.5

print "16-QAM, average power: {0:.4f}".format(p)

plt.scatter(a.real, a.imag)
const_plot()
for i, x in enumerate(a):
    s = "{0:04b}".format(i)[::-1]
    plt.text(x.real, x.imag+0.1, s, ha='center')

plt.show()