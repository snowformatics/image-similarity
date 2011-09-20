from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt


# imports specific to the plots in this example
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

# Twice as wide as it is tall.
fig = plt.figure(figsize=plt.figaspect(0.5))

#---- First subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
ax.set_zlim3d(-1.01, 1.01)

fig.colorbar(surf, shrink=0.5, aspect=10)


plt.show()

#import numpy
#from mayavi.mlab import *
#import time
#
#def test_surf():
#    """Test surf on regularly spaced co-ordinates like MayaVi."""
#    def f(x, y):
#        sin, cos = numpy.sin, numpy.cos
#        return sin(x+y) + sin(2*x - y) + cos(3*x+4*y)
#
#    x, y = numpy.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
#    s = surf(x, y, f)
#    #cs = contour_surf(x, y, f, contour_z=0)
#    #time.sleep(100)
#    #return s
#
#test_surf()