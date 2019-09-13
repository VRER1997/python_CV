from pylab import *
from PIL import Image

from PCV.localdescriptors import harris
from PCV.tools.imtools import imresize

im1 = array(Image.open("../data/sf_view1.jpg").convert('L'))
im2 = array(Image.open("../data/sf_view2.jpg").convert('L'))

im1 = imresize(im1, (im1.shape[1]/2, im1.shape[0]/2))
im2 = imresize(im2, (im2.shape[1]/2, im2.shape[0]/2))

wid = 5
harrisim = harris.compute_harris_response(im1, 5)
filter_coords1 = harris.get_harris_points(harrisim, wid+1)
d1 = harris.get_descriptors(im1, filter_coords1, wid)


harrisim = harris.compute_harris_response(im2, 5)
filter_coords2 = harris.get_harris_points(harrisim, wid+1)
d2 = harris.get_descriptors(im2, filter_coords2, wid)

matches = harris.match_twosided(d1, d2)

figure()
gray()
harris.plot_matches(im1, im2, filter_coords1, filter_coords2, matches)
show()