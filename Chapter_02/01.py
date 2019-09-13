from pylab import *
from PIL import Image
from PCV.localdescriptors import harris
from numpy import *

im = asarray(Image.open('1.jpeg').convert('L'))

harrisim = harris.compute_harris_response(im)

harrisim1 = 255 - harrisim

figure()
gray()

subplot(141)
imshow(harrisim1)

threshold = [0.01, 0.05, 0.1]

for i, thres in enumerate(threshold):
    filtered_coords = harris.get_harris_points(harrisim, 10, thres)
    subplot(1, 4, i+2)
    imshow(im)
    plot([p[1] for p in filtered_coords], [p[0] for p in filtered_coords], '*')
    axis('off')

show()

