#-3966,582123    -3785,483453    -3598,894653    -3405,126226    -3205,657883
#
#fig=figure()
#ax = fig.add_subplot(111,projection="3d")
#
#x = [-3966.582123,-3785.483453,-3598.894653,-3405.126226,-3205.657883]
#y = [1,2,3,4,5]
#z = [1]
#
#ax.plot(x,y,z)
#ax.grid(on=False)
#show()

import numpy
from mayavi.mlab import *

def test_surf():
    """Test surf on regularly spaced co-ordinates like MayaVi."""
    def f(x, y):
        sin, cos = numpy.sin, numpy.cos
        return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)

    x, y = numpy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
    s = surf(x, y, f)
    #cs = contour_surf(x, y, f, contour_z=0)
    return s