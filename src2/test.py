from PIL import Image
from scipy import stats as P
import os
import time
#start = time.clock()
#
#pics = os.listdir("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test")
#index1 = 0
#index2 = 0
#f = open('out.txt', 'w')
#for x in range(len(pics)):
#    im = Image.open("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test\\" + pics[index1])
#    for pic in pics:
#        im2 = Image.open("E:\User Data\mikroskop\Eigene Dateien\Python\image compare\src\\test\\" + pics[index2])
#        im = im.resize((200, 800))
#        data = list(im.getdata())
#        lst1 = []
#        for i in data:
#            lst1.append(i[0])
#        im2 = im2.resize((200, 800))
#        data2 = list(im2.getdata())
#        lst2 = []
#        for i2 in data2:
#            lst2.append(i2[0])
#        p_value = P.pearsonr(lst1, lst2)
#        f.write(pics[index1] + '\t' + pics[index2] + '\t' + str(p_value) + '\n')
#        index2 = index2 + 1
#    index1 = index1 + 1
#    index2 = 0
#end = time.clock()
#print end-start   

im = Image.open('09B_084_01.jpg')
im = im.resize((50, 200))
data = list(im.getdata())
lst1 = []
for i in data:
    lst1.append(i[0])

im2 = Image.open('09B_085_01.jpg')
im2 = im2.resize((50, 200))
data2 = list(im2.getdata())
lst2 = []
for i2 in data2:
    lst2.append(i2[0])
print len(lst1), len(lst2)
print P.pearsonr(lst1, lst2)
