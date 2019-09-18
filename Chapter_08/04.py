from PCV.localdescriptors import dsift
from PCV.tools import imtools
import os

path = ['train/', 'test/']

for p in path:
    npath = "../data/uniform/" + p
    imlist = [os.path.join(npath, f) for f in os.listdir(npath)]
    print len(imlist)

    for filename in imlist:
        featfile = filename[:-3] + 'dsift'
        dsift.process_image_dsift(filename, featfile, 10, 5, resize=(50, 50))
        
    print path, " over"
