from PCV.tools import imtools
import pickle
from scipy.cluster.vq import *

imlist = imtools.get_imlist('../data/fontimages/a_thumbs/')
imnbr = len(imlist)
