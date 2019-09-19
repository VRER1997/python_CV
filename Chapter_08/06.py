from PCV.tools import pca
from PCV.localdescriptors import sift, dsift
from PCV.classifiers import bayes
import numpy as np
import os

def read_gesture_features_labels(path):
    featlist = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.dsift')]
    print len(featlist)

    features = []
    for featfile in featlist:
        l, d = sift.read_features_from_file(featfile)
        features.append(d.flatten())

    features = np.array(features)

    label = [featfile.split('/')[-1].split('-')[0] for featfile in featlist]
    print label[:5]
    return features, np.array(label)


features, labels = read_gesture_features_labels("../data/uniform/train/")
features_test, labels_test = read_gesture_features_labels("../data/uniform/test/")

V, S, m = pca.pca(features)

V = V[:50]
features = np.array([np.dot(V, f-m) for f in features])
features_test = np.array([np.dot(V, f-m) for f in features_test])

classnames = ['A', 'B', 'C', 'Five', 'Point', 'V']

bc = bayes.BayesClassifier()
blist = [features[np.where(labels == c)[0]] for c in classnames]

bc.train(blist, classnames)
res = bc.classify(features_test)[0]

acc = np.sum(1.0 * (res == labels_test)) / len(labels_test)
print "ACC: ", acc

