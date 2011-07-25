#!/usr/bin/python
import Image
import numpy
import sys
import time
import os
import re
import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
from multiprocessing import Process

def get(i):
    data = imread(i)
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    return (data - data.mean()) / data.std()

index1 = 0
index2 = 0
ready_lst = set()
final_list = []
#f = open('/home/cuda/Stefanie/HOST01to07/out.txt', 'a')
project_lst = ["HS01", "HS02", "HS03", "HS04", "HS05", "HS06", "HS07"]
shots = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
slides = ["A", "B"]

def cross_corr(project):
    f = open('/home/cuda/Stefanie/HOST01to07/out' + project + '.txt', 'w')
    for project in project_lst:
        for shot in shots:
            for slide in slides:
                index1 = 0
                pict_lst = os.listdir("/home/cuda/Stefanie/images75/" + project + "/" + shot + "/" +  slide + "/")
                for x in range(len(pict_lst)):
                    im = "/home/cuda/Stefanie/images75/" + project + "/" + shot + "/" +  slide + "/" + pict_lst[index1]
                    
                    for pic in pict_lst:
                        im2 = "/home/cuda/Stefanie/images75/" + project + "/" + shot + "/" +  slide + "/" + pict_lst[index2]
                        if (pict_lst[index2], pict_lst[index1]) not in ready_lst:
                            data1 = get(im)
                            data2 = get(im2)
                            cc = c2d(data1, data2, mode='same')
                            f.write(project + '\t' + pict_lst[index1] + '\t' + pict_lst[index2] + '\t' + str(cc.max()) + '\n')
                            ready_lst.add((pict_lst[index1], pict_lst[index2]))
                            #print project, shot, slide, pict_lst[index1], pict_lst[index2], cc.max()
                    
                        index2 = index2 + 1
                        
                    index1 = index1 + 1
                    index2 = 0
            ready_lst.clear()

### start processes
def main_processes(): 
    
    for i in xrange(7): 
        p = Process(target=cross_corr, args=(liste[i]))
        p.start() 
    
if __name__ == "__main__": 
    main_processes()

