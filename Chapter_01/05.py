from PIL import Image
from pylab import *
from scipy.ndimage import filters
import numpy as np

im = np.asarray(Image.open('1.jpeg').convert('L'))

figure()
gray()
subplot(1, 4, 1)
title('[Origin]')
imshow(im)
show()

for bin, blur in enumerate([2, 5, 10]):
    im2 = np.zeros(im.shape)
    im2 = filters.gaussian_filter(im, blur)
    im2 = np.uint8(im2)
    imNum = str(blur)
    subplot(1, 4, 2+bin)
    title('blur=' + imNum)
    imshow(im2)

show()