from PIL import Image
from pylab import *
import numpy as np
from scipy.ndimage import filters
from PCV.tools import rof

im = np.asarray(Image.open('1.jpeg').convert('L'))
U, T = rof.denoise(im, im)
G = filters.gaussian_filter(im, 3)

figure()
gray()

subplot(131)
imshow(im)

subplot(132)
imshow(G)

subplot(133)
imshow(U)

show()