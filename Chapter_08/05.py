import os
from PCV.localdescriptors import sift
from PCV.classifiers import knn
import numpy as np

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

k = 1
knn_classifier = knn.KnnClassifier(labels, features)
res = np.array([knn_classifier.classify(features_test[i], k) for i in range(len(features_test))])

acc = sum(1.0 * (res == labels_test)) / len(labels_test)
print "Acc ", acc

def print_confusion(res, labels, classname):
    n = len(classname)
    class_ind = dict([(classname[i], i) for i in range(n)])

    print class_ind

    confuse = np.zeros((n, n))
    for i in range(len(labels_test)):
        confuse[class_ind[res[i]], class_ind[labels_test[i]]] += 1

    print classname
    print confuse

classnames = ['A', 'B', 'C', 'Five', 'Point', 'V']
print_confusion(res, labels_test, classnames)