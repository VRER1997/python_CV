import PCV.geometry.sfm as sfm
from load_vggdata import *
from pylab import *

ndx = (corr[:, 0] >= 0) & (corr[:, 1] >= 0)

x1 = point2D[0][:, corr[ndx, 0]]
x1 = vstack((x1, ones(x1.shape[1])))
x2 = point2D[1][:, corr[ndx, 1]]
x2 = vstack((x2, ones(x2.shape[1])))

F = sfm.compute_fundamental(x1, x2)
e = sfm.compute_epipole(F)

figure()
imshow(im1)

for i in range(5):
    sfm.plot_epipolar_line(im1, F, x2[:, i], e, False)
axis('off')


figure()
imshow(im2)
for i in range(5):
    plot(x2[0,i], x2[1,i], 'o')
axis('off')

show()

