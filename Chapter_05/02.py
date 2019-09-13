from mpl_toolkits.mplot3d import axes3d
from pylab import *
from load_vggdata import *
from numpy import *

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(point3D[0],point3D[1],point3D[2], 'k.')
show()