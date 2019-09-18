from PCV.localdescriptors import dsift, sift
import numpy as np
from PIL import Image
from pylab import *

dsift.process_image_dsift('../data/empire.jpg', 'empire.sift', 90, 40, True)
l, d = sift.read_features_from_file('empire.sift')

im = np.array(Image.open('../data/empire.jpg'))
sift.plot_features(im, l, True)
show()