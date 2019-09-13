from PCV.geometry import sfm, camera
from load_vggdata import *
from pylab import *

corr = corr[:, 0]
ndx3D = where(corr>=0)[0]
ndx2D = corr[ndx3D]

x = point2D[0][:, ndx2D]
x = vstack((x, ones(x.shape[1])))
X = point3D[:, ndx3D]
X = vstack((X, ones(X.shape[1])))

Pest = camera.Camera(sfm.compute_P(x,X))

print Pest.P / Pest.P[2,3]
print P[0].P / P[0].P[2,3]

Xest = Pest.project(X)

figure()
imshow(im1)
plot(x[0], x[1], 'bo')
plot(Xest[0], Xest[1], 'r.')
axis('off')

show()