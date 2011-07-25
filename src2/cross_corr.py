import Image
import numpy
import sys
import time
import os
import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d

start = time.clock()

def get(i):
    # get JPG image as Scipy array, RGB (3 layer)
    data = imread(i)
    # convert to grey-scale using W3C luminance calc
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    # normalize per http://en.wikipedia.org/wiki/Cross-correlation
    return (data - data.mean()) / data.std()

pics = os.listdir("D:\\src\\test_resize75")
index1 = 0
index2 = 0
f = open('out.txt', 'w')
for x in range(len(pics)):
    im = "D:\\src\\test_resize75\\" + pics[index1]
    #print pics
    for pic in pics:
        im2 = "D:\\src\\test_resize75\\" + pics[index2]
        data1 = get(im)
        data2 = get(im2)
        cc = c2d(data1, data2, mode='same')
        f.write(pics[index1] + '\t' + pics[index2] + '\t' + str(cc.max()) + '\n')
        print pics[index1], pics[index2], cc.max()
        
        index2 = index2 + 1
    index1 = index1 + 1
    index2 = 0
end = time.clock()
print end-start 
f.close()

