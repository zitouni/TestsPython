import matplotlib

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


import ieee802_11
c = ieee802_11.constellation_16qam()
a = np.array(c.points())
p = np.average(np.abs(a)**2)
level = .1**.5

def const_plot():
    plt.axis('off')
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.arrow(-1.2, 0, 2.4, 0, head_width=0.05, head_length=0.1, fc='gray', ec='gray')
    plt.arrow(0, -1.2, 0, 2.4, head_width=0.05, head_length=0.1, fc='gray', ec='gray')
    plt.xlim(-1.4, 1.4)
    plt.ylim(-1.5, 1.5)

N = 1000
data = np.random.randint(0, 16, N)
orig_const = a[data]


noisy_const = orig_const + np.random.sample(N) * 2 * level - level +\
                           np.random.sample(N) * 2j * level - level * 1j

rx = np.array(map(lambda x: c.decision_maker_v([x]), noisy_const))
rx_const = a[rx]

if any(rx != data):
    print "16-QAM: data does not match."
else:
    print "16-QAM: points decoded successfully."

plt.scatter(a.real, a.imag)
plt.scatter(noisy_const.real, noisy_const.imag, marker='x')
const_plot()
for d, x, y in zip(rx, rx_const, noisy_const):
    plt.plot([x.real, y.real], [x.imag, y.imag], color=mpl.cm.hsv(d/16.0))

plt.show()