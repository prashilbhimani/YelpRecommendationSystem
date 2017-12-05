
# coding: utf-8

# In[1]:

import json


# In[2]:

business = []
for b in open('Dataset/json_dataset/az_business.json', encoding="utf8"):
    business.append(json.loads(b))


# In[6]:

def getSubsetDict(attributes,original):
    temp={}
    for a in attributes:
        temp[a]=original[a]
    return temp


# In[8]:

for i in range(0,len(business)):
    attributes=['business_id','name','neighborhood','city','state','stars','attributes','categories']
    business[i]=getSubsetDict(attributes,business[i])


# In[11]:

with open("Dataset/JSON_Dataset/sub_az_business.json","w") as outfile:
    for r in business:
        json.dump(r,outfile)
        outfile.write("\n")

