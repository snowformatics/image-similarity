import Image
import numpy
import sys
import time
import os

start = time.clock()
#def main(img1, img2):
#    
#    img2 = img2.resize((50, 200))
#    img1 = img1.resize((50, 200))
#    if img1.size != img2.size or img1.getbands() != img2.getbands():
#        return -1
#    s = 0
#    for band_index, band in enumerate(img1.getbands()):
#        m1 = numpy.array([p[band_index] for p in img1.getdata()]).reshape(*img1.size)
#        m2 = numpy.array([p[band_index] for p in img2.getdata()]).reshape(*img2.size)
#        s += numpy.sum(numpy.abs(m1-m2))
#    print s, img1
#    
#img1 = Image.open('base.png')
#img2 = Image.open('image2.png')
#main(img1, img2)


pics = os.listdir("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test")
index1 = 0
index2 = 0
f = open('out.txt', 'w')
for x in range(len(pics)):
    im = Image.open("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test\\" + pics[index1])
    for pic in pics:
        im2 = Image.open("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test\\" + pics[index2])
        #img2 = im2
        #img1 = im
#        if img1.size != img2.size or img1.getbands() != img2.getbands():
#            return -1
        s = 0
        for band_index, band in enumerate(img1.getbands()):
            m1 = numpy.array([p[band_index] for p in img1.getdata()]).reshape(*img1.size)
            m2 = numpy.array([p[band_index] for p in img2.getdata()]).reshape(*img2.size)
            s += numpy.sum(numpy.abs(m1-m2))

        f.write(pics[index1] + '\t' + pics[index2] + '\t' + str(s) + '\n')

        index2 = index2 + 1
    index1 = index1 + 1
    index2 = 0
end = time.clock()
print end-start   