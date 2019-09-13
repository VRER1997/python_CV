from PIL import Image
from pylab import *

im = Image.open('1.jpeg')
figure()

imshow(im)
x = [50, 75, 100, 150]
y = [100, 100, 200, 200]
plot(x, y, 'r*')
plot(x[:2], y[:2])
title('[Plot]')

show()