from PIL import Image
import numpy


im1 = "09B_084_01.jpg"
im2 = "09B_085_01.jpg"
im3 = "2-3.jpg"
im4 = "belichtung1.jpg"
im5 = "belichtung2.jpg"
im6 = 'unterschiedlich1.jpg'
im7 = 'unterschiedlich2.jpg'

im = Image.open(im4)
im = im.resize((50, 200))
  
r = numpy.asarray(im.convert( "RGB", (1,0,0,0, 1,0,0,0, 1,0,0,0) ))
g = numpy.asarray(im.convert( "RGB", (0,1,0,0, 0,1,0,0, 0,1,0,0) ))
b = numpy.asarray(im.convert( "RGB", (0,0,1,0, 0,0,1,0, 0,0,1,0) ))
hr, h_bins = numpy.histogram(r, bins=256, normed=True)
hg, h_bins = numpy.histogram(g, bins=256, normed=True)
hb, h_bins = numpy.histogram(b, bins=256, normed=True)
hist1 = numpy.array([hr, hg, hb]).ravel()

im = Image.open(im5)
im = im.resize((50, 200))
r = numpy.asarray(im.convert( "RGB", (1,0,0,0, 1,0,0,0, 1,0,0,0) ))
g = numpy.asarray(im.convert( "RGB", (0,1,0,0, 0,1,0,0, 0,1,0,0) ))
b = numpy.asarray(im.convert( "RGB", (0,0,1,0, 0,0,1,0, 0,0,1,0) ))
hr, h_bins = numpy.histogram(r, bins=256, normed=True)
hg, h_bins = numpy.histogram(g, bins=256, normed=True)
hb, h_bins = numpy.histogram(b, bins=256, normed=True)
hist2 = numpy.array([hr, hg, hb]).ravel()


diff = hist1 - hist2
distance = numpy.sqrt(numpy.dot(diff, diff))
print distance