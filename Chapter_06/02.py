from PCV.tools import imtools
import pickle
from scipy.cluster.vq import *
from PIL import Image
from PCV.tools import pca
from pylab import *
imlist = imtools.get_imlist('../data/fontimages/a_thumbs/')

im = array(Image.open(imlist[0]))
n, m = im.shape[:2]

imlist = imlist[:200]
imnbr = len(imlist)
immatrix = np.array([np.array(Image.open(im)).flatten() for im in imlist], 'f')

V, S, immean = pca.pca(immatrix)

figure()
gray()
subplot(2, 4, 1)
imshow(immean.reshape(m, n))
for i in range(7):
    subplot(2, 4, i+2)
    imshow(V[i].reshape(m, n))

show()

immean = immean.flatten()
projected = array([dot(V[:40], immatrix[i]-immean) for i in range(imnbr)])
projected = whiten(projected)
centroid, distortion = kmeans(projected, 4)
code, distance = vq(projected, centroid)

for k in range(4):
    ind = where(code==k)[0]
    figure()
    gray()
    for i in range(min(len(ind), 40)):
        subplot(4, 10, i+1)
        imshow(immatrix[ind[i]].reshape((25, 25)))
        axis('off')

show()
