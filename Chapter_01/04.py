from PIL import Image
from pylab import *
from PCV.tools import imtools
import numpy as np


im = np.array(Image.open('1.jpeg').convert('L'))
im2, cdf = imtools.histeq(im)

figure()

subplot(121)
hist(im.flatten(), 128)

subplot(122)
hist(im2.flatten(), 128)

show()