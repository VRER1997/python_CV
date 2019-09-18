import pickle
from PCV.imagesearch import imagesearch
from PCV.localdescriptors import sift
from sqlite3 import dbapi2 as sqlite
from PCV.tools.imtools import get_imlist
import os

path = "F:\\BaiduNet\\ukbench\\full\\"
imlist = [os.path.join(path, f) for f in os.listdir(path)]
imnbr = len(imlist)
featlist = [imlist[i].split('\\')[-1][:-3] + 'sift'for i in range(imnbr)]

with open('vocabulary.pkl', 'rb') as f:
    voc = pickle.load(f)

index = imagesearch.Indexer('testImgAdd.db', voc)
index.create_tables()

for i in range(imnbr)[:500]:
    locs, descr = sift.read_features_from_file(featlist[i])
    index.add_to_index(imlist[i], descr)

index.db_commit()

con = sqlite.connect('testImgAdd.db')
print con.execute('select * from imlist').fetchone()