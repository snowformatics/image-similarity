import Image
import numpy
import sys
import time
import os
import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d

from numpy import *
import pylab as p
#import matplotlib.axes3d as p3
import mpl_toolkits.mplot3d.axes3d as p3


def get(i):
    # get JPG image as Scipy array, RGB (3 layer)
    data = imread(i)
    # convert to grey-scale using W3C luminance calc
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    # normalize per http://en.wikipedia.org/wiki/Cross-correlation
    return (data - data.mean()) / data.std()


im1 = "09B_084_01.jpg"
im2 = "09B_084_01.jpg"
im3 = "2-3.jpg"
data1 = get(im1)
data2 = get(im3)
cc = c2d(data1, data2, mode='same')
f = open('out.txt', 'w')
for i in cc:
    
    for x in i:
        f.write(str(x) + '\t')
    f.write('\n')
        
f.close()
print str(cc.max())
        

#fig=p.figure()
#ax = p3.Axes3D(fig)
## x, y, and z are 100x100 arrays
#ax.plot_surface(cc)
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')
#p.show()


