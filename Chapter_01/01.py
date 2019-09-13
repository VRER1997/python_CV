from PIL import Image
from pylab import *

figure()

pil_im = Image.open("1.jpeg")
gray()
subplot(221)
title('[Origin]')
imshow(pil_im)

pil_im_gray = Image.open('1.jpeg').convert('L')
subplot(222)
title('[gray]')
imshow(pil_im)

size= 128, 128
pil_im.thumbnail(size)
subplot(223)
title('[thumbnail]')
imshow(pil_im)

pil_im = Image.open('1.jpeg').rotate(45)
subplot(224)
title('[rotate]')
imshow(pil_im)

show()