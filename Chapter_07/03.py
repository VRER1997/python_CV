# -*- coding: utf-8 -*-
import pickle
from PCV.localdescriptors import sift
from PCV.imagesearch import imagesearch
from PCV.geometry import homography
from PCV.tools.imtools import get_imlist

import os
path = "F:\\BaiduNet\\ukbench\\full\\"
imlist = [os.path.join(path, f) for f in os.listdir(path)]
imnbr = len(imlist)
featlist = [imlist[i].split('\\')[-1][:-3] + 'sift'for i in range(imnbr)]
with open('vocabulary.pkl', 'rb') as f:
    voc = pickle.load(f)

src = imagesearch.Searcher('testImgAdd.db', voc)

q_ind = 0
nbr_results = 20

res_reg = [w[1] for w in src.query(imlist[q_ind])[:nbr_results]]
print 'top matches (regular) : ', res_reg

q_locs, q_descr = sift.read_features_from_file(featlist[q_ind])
fp = homography.make_homog(q_locs[:, :2].T)

model = homography.RansacModel()
rank = {}

for ndx in res_reg[1:]:
    locs, descr = sift.read_features_from_file(featlist[ndx])
    matches = sift.match(q_descr, descr)
    ind = matches.nonzero()[0]
    ind2 = matches[ind]
    tp = homography.make_homog(locs[:, :2].T)
    try:
        H, inliners = homography.H_from_ransac(fp[:, ind], tp[:, ind2], model, match_theshold=4)
    except:
        inliners = []
    rank[ndx] = len(inliners)

sorted_rank = sorted(rank.items(), key=lambda t: t[1], reverse=True)
res_geom = [res_reg[0]] + [s[0] for s in sorted_rank]
# 显示查询结果
imagesearch.plot_results(src, res_reg[:8]) #常规查询
imagesearch.plot_results(src, res_geom[:8]) #重排后的结果
