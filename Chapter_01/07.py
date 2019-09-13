from PIL import Image
from scipy.ndimage import measurements, morphology
from pylab import *
import numpy as np

im = np.asarray(Image.open('house.png'))

figure()
gray()
subplot(221)
title('[Origin]')
imshow(im)

label, nbr_objects = measurements.label(im)
print "Number of objects: " , nbr_objects
subplot(222)
title('[1]')
imshow(label)

im_open = morphology.binary_opening(im, ones((5, 5)), iterations=2)
subplot(223)
title('[2]')
imshow(im_open)

label_open, nbr_objects_open = measurements.label(im_open)
print "Number of ojects: ", nbr_objects_open
subplot(224)
imshow(label_open)
title('[3]')

show()