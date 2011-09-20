import Image
import numpy
import sys

im1 = "09B_084_01.jpg"
im2 = "09B_085_01.jpg"
im3 = "2-3.jpg"
im4 = "belichtung1.jpg"
im5 = "belichtung2.jpg"
im6 = 'unterschiedlich1.jpg'
im7 = 'unterschiedlich2.jpg'

img1 = Image.open(im2)
img2 = Image.open(im2)

img1 = img1.resize((50, 200))
img2 = img2.resize((50, 200))

s = 0
for band_index, band in enumerate(img1.getbands()):
    m1 = numpy.fft.fft2(numpy.array([p[band_index] for p in img1.getdata()]).reshape(*img1.size))
    m2 = numpy.fft.fft2(numpy.array([p[band_index] for p in img2.getdata()]).reshape(*img2.size))
    print m1
    print m2
    s += numpy.sum(numpy.abs(m1-m2))
print s

