
# coding: utf-8

# In[1]:

import json


# In[2]:

business = []
for b in open('Dataset/json_dataset/sub_az_business.json', encoding="utf8"):
    business.append(json.loads(b))


# In[13]:

business_review={}
for b in business:
    business_review[b['business_id']]=[]


# In[4]:

reviews = []
for r in open('Dataset/json_dataset/sub_az_review.json', encoding="utf8"):
    reviews.append(json.loads(r))


# In[14]:

for r in reviews:
    business_review[r['business_id']].append(r['text'])


# In[15]:

with open("Dataset/JSON_Dataset/az_business_review.json","w") as outfile:
    json.dump(business_review,outfile)
    outfile.write("\n")


# In[ ]:



