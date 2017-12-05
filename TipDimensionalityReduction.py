
# coding: utf-8

# In[1]:

import json


# In[3]:

tips = []
for t in open('Dataset/json_dataset/az_tip.json', encoding="utf8"):
    tips.append(json.loads(t))


# In[4]:

def getSubsetDict(attributes,original):
    temp={}
    for a in attributes:
        temp[a]=original[a]
    return temp


# In[6]:

for i in range(0,len(tips)):
    attributes=['text', 'business_id', 'user_id']
    tips[i]=getSubsetDict(attributes,tips[i])


# In[7]:

with open("Dataset/JSON_Dataset/sub_az_tip.json","w") as outfile:
    for t in tips:
        json.dump(t,outfile)
        outfile.write("\n")


# In[ ]:



