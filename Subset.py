
# coding: utf-8

# In[2]:

import json

business = []
for b in open('Dataset/JSON_Dataset/business.json', encoding="utf8"):
    business.append(json.loads(b))

state={}
az_business={}
business_list=[]
for b in business:
    if b["state"]=="AZ":
        az_business[b["business_id"]]=[]
        business_list.append(b)


# In[ ]:




# In[5]:

reviews = []
for review in open('Dataset/JSON_Dataset/review.json', encoding="utf8"):
    reviews.append(json.loads(review))


# In[6]:

az_business_review=[]
for r in reviews:
    if r["business_id"] in az_business:
        az_business[r["business_id"]].append(r["review_id"])
        az_business_review.append(r)



with open("Dataset/JSON_Dataset/az_business.json","w") as outfile:
    for b in business_list:
        json.dump(b,outfile)


# In[8]:

with open("Dataset/JSON_Dataset/az_review.json","w") as outfile:
    for r in az_business_review:
        json.dump(r,outfile)





