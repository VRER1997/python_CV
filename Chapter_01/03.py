from PIL import Image
from pylab import *
import numpy as np

im = np.array(Image.open('1.jpeg').convert('L'))

figure()
subplot(121)
gray()
contour(im, origin='image')
axis('equal')
title('[contour]')

subplot(122)
hist(im.flatten(), 128)
title('[hist]')

show()