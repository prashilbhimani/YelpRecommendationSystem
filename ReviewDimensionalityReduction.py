
# coding: utf-8

# In[1]:

import json


# In[2]:

reviews = []
for r in open('Dataset/json_dataset/az_review.json', encoding="utf8"):
    reviews.append(json.loads(r))


# In[3]:

def getSubsetDict(attributes,original):
    temp={}
    for a in attributes:
        temp[a]=original[a]
    return temp


# In[4]:

for i in range(0,len(reviews)):
    attributes=['review_id', 'user_id', 'business_id','stars', 'text']
    reviews[i]=getSubsetDict(attributes,reviews[i])


# In[5]:

with open("Dataset/JSON_Dataset/sub_az_review.json","w") as outfile:
    for r in reviews:
        json.dump(r,outfile)
        outfile.write("\n")

