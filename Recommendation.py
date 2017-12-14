
# coding: utf-8

# In[1]:

import json
import heapq


# In[2]:

business_tags = {}
for b in open('Dataset/az_all_business_features.json', encoding="utf8"):
    business_tags=json.loads(b)


# In[3]:

user_tags = {}
for b in open('Dataset/az_all_user_features.json', encoding="utf8"):
    user_tags=json.loads(b)


# In[4]:

user_postal = {}
for b in open('Dataset/user_postal.json', encoding="utf8"):
    user_postal=json.loads(b)


# In[5]:

business_postal = {}
for b in open('Dataset/postal_business.json', encoding="utf8"):
    business_postal=json.loads(b)


# In[6]:

user_business = {}
for b in open('Dataset/user_business_gt3.json', encoding="utf8"):
    user_business=json.loads(b)


# In[9]:

j=0
user_recommendation={}
user_keys=list(user_postal.keys())
for u in user_keys[1:20000]:
    user_recommendation[u]=[]
    for up in user_postal[u]:
        for b in business_postal[up]:
            if b not in user_business[u] and b in business_tags:
                try:
                    b_tags=set(business_tags[b])
                    u_tags=set(user_tags[u])
                    c_tags=u_tags.intersection(b_tags)
                    if 0.7*len(b_tags)<len(c_tags):
                        heapq.heappush(user_recommendation[u], (len(c_tags),b))
                except:
                    pass
    user_recommendation[u]=user_recommendation[u][:100]
    print(j)
    j=j+1


# In[ ]:

with open("Dataset/JSON_Dataset/az_recommendation.json","w") as outfile:
    json.dump(user_recommendation,outfile)
    outfile.write("\n")

