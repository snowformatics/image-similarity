import Image
import numpy
import sys
import time
import os
import re
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

index1 = 0
index2 = 0
ready_lst = set()
final_list = []
f = open('out.txt', 'w')


project_lst = ["HS01"]
#project_lst = ["HS01"]
shots = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
slides = ["A", "B"]
#slides = ["B"]
#shots = ["01"]
for project in project_lst:
    for shot in shots:
        for slide in slides:
            index1 = 0
            pict_lst = os.listdir("D:\Stefanie\HOST\\" + project + "\\" + shot + "\\" +  slide + "\\")
            #for pict_id in pict_lst:
            for x in range(len(pict_lst)):
                #print project, shot, slide, pict_id
                #print index1
                im = "D:\Stefanie\HOST\\" + project + "\\" + shot + "\\" +  slide + "\\" + pict_lst[index1]
                
                for pic in pict_lst:
                    im2 = "D:\Stefanie\HOST\\" + project + "\\" + shot + "\\" +  slide + "\\" + pict_lst[index2]
                    if (pict_lst[index2], pict_lst[index1]) not in ready_lst:
                        data1 = get(im)
                        data2 = get(im2)
                        cc = c2d(data1, data2, mode='same')
                        f.write(project + '\t' + pict_lst[index1] + '\t' + pict_lst[index2] + '\t' + str(cc.max()) + '\n')
                        #final_list.append((project, pict_lst[index1], pict_lst[index2], str(cc.max())))
                        ready_lst.add((pict_lst[index1], pict_lst[index2]))
                        #print project, shot, slide, pict_lst[index1], pict_lst[index2], cc.max()
                
                    index2 = index2 + 1
                    
                index1 = index1 + 1
                index2 = 0
        ready_lst.clear()
#for i in final_list:
#    f.write(str(i) + '\n')
f.close()
end = time.clock()
print end-start






