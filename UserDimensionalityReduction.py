
# coding: utf-8

# In[1]:

import json


# In[2]:

users = []
for u in open('Dataset/json_dataset/az_user.json', encoding="utf8"):
    users.append(json.loads(u))


# In[3]:

def getSubsetDict(attributes,original):
    temp={}
    for a in attributes:
        temp[a]=original[a]
    return temp


# In[4]:

for i in range(0,len(users)):
    attributes=['user_id', 'name', 'friends']
    users[i]=getSubsetDict(attributes,users[i])


# In[5]:

with open("Dataset/JSON_Dataset/sub_az_user.json","w") as outfile:
    for u in users:
        json.dump(u,outfile)
        outfile.write("\n")


# In[ ]:



