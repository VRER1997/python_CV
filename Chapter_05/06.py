from PCV.geometry import homography, sfm
from PCV.localdescriptors import sift
import numpy as np
from PIL import Image
from pylab import *

K = np.array([[2394, 0, 932], [0, 2398, 628], [0, 0, 1]])

imname = '../data/alcatraz1.jpg'
im2name = '../data/alcatraz2.jpg'

im1 = np.array(Image.open(imname))
sift.process_image(imname, 'im1.sift')
l1, d1 = sift.read_features_from_file('im1.sift')

im2 = np.array(Image.open(im2name))
sift.process_image(im2name, 'im2.sift')
l2, d2 = sift.read_features_from_file('im2.sift')

matches = sift.match_twosided(d1, d2)
ndx = matches.nonzero()[0]

x1 = homography.make_homog(l1[ndx, :2].T)
ndx2 = [int(matches[i]) for i in ndx]
x2 = homography.make_homog(l2[ndx2, :2].T)

x1n = np.dot(np.linalg.inv(K), x1)
x2n = np.dot(np.linalg.inv(K), x2)

model = sfm.RansacModel()
E, inliners = sfm.F_from_ransac(x1n, x2n, model)

P1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
P2 = sfm.compute_P_from_essential(E)

ind = 0
maxres = 0
infront = 0
for i in range(4):
    X = sfm.triangulate(x1n[:, inliners], x2n[:, inliners], P1, P2[i])
    d1 = np.dot(P1, X)[2]
    d2 = np.dot(P2[i], X)[2]
    if sum(d1 > 0) + sum(d2 > 0) > maxres:
        maxres = sum(d1 > 0) + sum(d2 > 0)
        ind = i
        infront = (d1 > 0) & (d2 > 0)

X = sfm.triangulate(x1n[:, inliners], x2n[:, inliners], P1, P2[ind])
X = X[:, infront]

from mpl_toolkits.mplot3d import axes3d

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(-X[0], X[1], X[2], 'k.')
axis('off')

from PCV.geometry import camera

cam1 = camera.Camera(P1)
cam2 = camera.Camera(P2[ind])
x1p = cam1.project(X)
x2p = cam2.project(X)

x1p = np.dot(K, x1p)
x2p = np.dot(K, x2p)

figure()
imshow(im1)
gray()
plot(x1p[0], x1p[1], 'o')
plot(x1[0], x1[1], 'r.')
axis('off')

figure()
imshow(im2)
gray()
plot(x2p[0], x2p[1], 'o')
plot(x2[0], x2[1], 'r.')
axis('off')
show()
