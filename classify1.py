from csv import DictReader, DictWriter

import numpy as np
from numpy import array
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split

kTARGET_FIELD = 'spoiler'
kTEXT_FIELD = 'sentence'


class Featurizer:
    def __init__(self):
        #self.vectorizer = CountVectorizer()
        self.bigram_vectorizer = TfidfVectorizer(min_df=3, max_df=0.95)
    def train_feature(self, examples):
        return self.bigram_vectorizer.fit_transform(examples)

    def test_feature(self, examples):
        return self.bigram_vectorizer.transform(examples)

    def show_top10(self, classifier, categories):
        feature_names = np.asarray(self.bigram_vectorizer.get_feature_names())
        if len(categories) == 2:
            top10 = np.argsort(classifier.coef_[0])[-10:]
            bottom10 = np.argsort(classifier.coef_[0])[:10]
            print("Pos: %s" % " ".join(feature_names[top10]))
            print("Neg: %s" % " ".join(feature_names[bottom10]))
        else:
            for i, category in enumerate(categories):
                top10 = np.argsort(classifier.coef_[i])[-10:]
                print("%s: %s" % (category, " ".join(feature_names[top10])))

if __name__ == "__main__":

    # Cast to list to keep it all in memory
    train = list(DictReader(open("../data/spoilers/train.csv", 'r')))
    test = list(DictReader(open("../data/spoilers/test.csv", 'r')))
    xtrain, xtest = train_test_split(train, test_size=0.20, random_state=42)
    feat = Featurizer()
    # vec= DictVectorizer()
    # array1=vec.fit_transform(train).toarray()
    # print array1
    # print vec.get_feature_names()
    feat = Featurizer()

    labels = []
    for line in train:
        if not line[kTARGET_FIELD] in labels:
            labels.append(line[kTARGET_FIELD])

    print("Label set: %s" % str(labels))
    x_train = feat.train_feature(x[kTEXT_FIELD] for x in train)
    x_test = feat.test_feature(x[kTEXT_FIELD] for x in test)

    y_train = list(labels.index(x[kTARGET_FIELD])
                         for x in train)

    print(len(train), len(y_train))
    print(set(y_train))

    # Train classifier
    lr = SGDClassifier(loss='log', penalty='l2', shuffle=True)
    lr.fit(x_train, y_train)

    feat.show_top10(lr, labels)

    predictions = lr.predict(x_test)
    o = DictWriter(open("predictions_hem.csv", 'w'), ["Id", "spoiler"])
    o.writeheader()
    for ii, pp in zip([x['Id'] for x in test], predictions):
        d = {'Id': ii, 'spoiler': labels[pp]}
        o.writerow(d)