from PIL import Image
from pylab import *
from scipy.ndimage import filters
import numpy as np

im = np.asarray(Image.open('1.jpeg').convert('L'))
gray()

subplot(1, 4, 1)
title('[Origin]')
imshow(im)

imx = np.zeros(im.shape)
filters.sobel(im, 1, imx)
subplot(1, 4, 2)
title('[x]')
imshow(imx)

imy = np.zeros(im.shape)
filters.sobel(im, 0, imy)
subplot(1, 4, 3)
title('[y]')
imshow(imy)

mag = 255 - (imx**2 + imy**2) ** (0.5)
subplot(1, 4, 4)
title('[div]')
imshow(mag)

show()