from PIL import Image
from pylab import *
from load_vggdata import *

execfile('load_vggdata.py')

X = vstack((point3D, ones(point3D.shape[1])))
x = P[0].project(X)

figure()
imshow(im1)
plot(point2D[0][0], point2D[0][1], '*')
axis('off')

imshow(im1)
plot(x[0], x[1], 'r.')
axis('off')

show()