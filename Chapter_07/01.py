from PCV.localdescriptors import sift
import os
import pickle
from PCV.imagesearch import vocabulary

path = "F:\\BaiduNet\\ukbench\\full\\"
imlist = [os.path.join(path, f) for f in os.listdir(path)]
imnbr = len(imlist)
featlist = [imlist[i].split('\\')[-1][:-3] + 'sift'for i in range(imnbr)]

print featlist[0]

"""
for i in range(imnbr):

    sift.process_image(imlist[i], featlist[i])
"""

voc = vocabulary.Vocabulary('ukbenchtest')
voc.train(featlist[:1000], 1000, 10)

with open('vocabulary.pkl', 'wb') as f:
    pickle.dump(voc, f)
print 'vocabulary is : ', voc.name, voc.nbr_words