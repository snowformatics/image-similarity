from PIL import Image
import numpy
im = Image.open('base.png')
im = im.resize((50, 200))
  
r = numpy.asarray(im.convert( "RGB", (1,0,0,0, 1,0,0,0, 1,0,0,0) ))
g = numpy.asarray(im.convert( "RGB", (0,1,0,0, 0,1,0,0, 0,1,0,0) ))
b = numpy.asarray(im.convert( "RGB", (0,0,1,0, 0,0,1,0, 0,0,1,0) ))
hr, h_bins = numpy.histogram(r, bins=256, new=True, normed=True)
hg, h_bins = numpy.histogram(g, bins=256, new=True, normed=True)
hb, h_bins = numpy.histogram(b, bins=256, new=True, normed=True)
hist1 = numpy.array([hr, hg, hb]).ravel()

im = Image.open('image2.png')
im = im.resize((50, 200))
r = numpy.asarray(im.convert( "RGB", (1,0,0,0, 1,0,0,0, 1,0,0,0) ))
g = numpy.asarray(im.convert( "RGB", (0,1,0,0, 0,1,0,0, 0,1,0,0) ))
b = numpy.asarray(im.convert( "RGB", (0,0,1,0, 0,0,1,0, 0,0,1,0) ))
hr, h_bins = numpy.histogram(r, bins=256, new=True, normed=True)
hg, h_bins = numpy.histogram(g, bins=256, new=True, normed=True)
hb, h_bins = numpy.histogram(b, bins=256, new=True, normed=True)
hist2 = numpy.array([hr, hg, hb]).ravel()


diff = hist1 - hist2
distance = numpy.sqrt(numpy.dot(diff, diff))
print distance