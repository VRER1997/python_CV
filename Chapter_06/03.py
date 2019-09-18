from scipy.cluster.vq import *
from scipy.misc import imresize
import numpy as np
from PIL import Image
from pylab import *

step = 50
im = np.array(Image.open('../data/empire.jpg'))

dx = im.shape[0] / step
dy = im.shape[1] / step

features = []
for x in range(step):
    for y in range(step):
        R = np.mean(im[x*dx: (x+1)*dx, y*dy: (y+1)*dy, 0])
        G = np.mean(im[x*dx: (x+1)*dx, y*dy: (y+1)*dy, 1])
        B = np.mean(im[x*dx: (x+1)*dx, y*dy: (y+1)*dy, 2])
        features.append([R, G, B])

features = np.array(features, 'f')

centroids, variance = kmeans(features, 3)
code, distance = vq(features, centroids)

codeim = code.reshape(step, step)
codeim = imresize(codeim, im.shape[:2], interp='nearest')

figure()
imshow(codeim)
show()
