
# coding: utf-8

# In[1]:

from nltk.parse.stanford import StanfordDependencyParser
import json
import string
import re


# In[2]:

path_to_jar = 'stanford-corenlp-full/stanford-corenlp-3.8.0.jar'
path_to_models_jar = 'stanford-corenlp-full/stanford-corenlp-3.8.0-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)


# In[3]:

business = []
for b in open('Dataset/JSOn_Dataset/az_review.json', encoding="utf8"):
    business.append(json.loads(b))


# In[4]:

j=0
for b in business:
    print(b['text'])
    review=b['text'].lower().split(".")
    for r in review:
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        r=regex.sub('', r)
        print(r)
        result = dependency_parser.raw_parse(r)
        for dep in result:
            i=list(dep.triples())
        for a in i:
            #print(a)
            if a[1]=='nsubj' or a[1]=='amod' or a[1]=="advmod":
                print(a)
    print(" ")
    j=j+1
    if j>5:
        break


# In[ ]:




# In[ ]:



