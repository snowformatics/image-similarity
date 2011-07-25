from itertools import izip
import Image
 
i1 = Image.open("base.png")
i2 = Image.open("image2.png")
assert i1.mode == i2.mode, "Different kinds of images."
#assert i1.size == i2.size, "Different sizes."
 
pairs = izip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
ncomponents = i1.size[0] * i1.size[1] * 3
print "Difference (percentage):", (dif / 255.0 * 100) / ncomponents

## the function to compare the images
#def is_the_same(base, test_image):
#    for i in range(len(base)):
#        #print base[i], test_image[i]
#        #print ((base[i][0]-test_image[i][0])+(base[i][1]-test_image[i][1])+(base[i][2]-test_image[i][2]))
#        if (base[i] - test_image[i]) != 0:
#            return False
#    return True
#
#    
## set the test inputs; all images will be compared against base
#base = Image.open('base.png').getdata()
#bad = Image.open('image1.png').getdata()
#good = Image.open('image2.png')
#base = Image.open('base.png')
#bad = Image.open('image1.png')

import math, operator



rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
print rms

#def rmsdiff(im1, im2):
#    "Calculate the root-mean-square difference between two images"
#
#    h = ImageChops.difference(im1, im2).histogram()
#    # calculate rms
#    print type(h), type(im1.size[0])
#    return math.sqrt(reduce(operator.add,
#        map(lambda h, i: h*(i**2), h, range(256))
#    ) / (float(im1.size[0]) * im1.size[1]))
#
#rmsdiff(im1, im2)
#import Image
#import ImageChops
#
#
#
#diff = ImageChops.difference(im2, im1)
#print diff.getbbox()