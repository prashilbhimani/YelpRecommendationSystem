
# coding: utf-8

# In[32]:

import json
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from autocorrect import spell
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import numpy as np


# In[13]:

stemmer = SnowballStemmer("english",ignore_stopwords=True)


# In[7]:

business_review = []
for b in open('Dataset/json_dataset/az_business_review.json', encoding="utf8"):
    business_review=json.loads(b)


# In[47]:

j=0
for business_id in business_review.keys():
    new_reviews=[]
    for r in business_review[business_id]:
        print(r)
        words = word_tokenize(r)
        for w in words:
            new_reviews.append(spell(stemmer.stem(w)))
    new_reviews=' '.join(new_reviews)
    t=TfidfVectorizer( lowercase=True, analyzer='word', ngram_range=(1, ), use_idf=True, smooth_idf=True, stop_words='english')
    t.fit_transform([r])
    indices = np.argsort(t.idf_)[::-1]
    features = t.get_feature_names()
    top_n = 10
    top_features = [features[i] for i in indices[:top_n]]
    print (top_features)
    j=j+1
    if j>5:
        break


# In[ ]:



