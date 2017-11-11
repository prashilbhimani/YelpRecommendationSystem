
# coding: utf-8

# In[1]:

import json


# In[2]:

az_business = {}
for b in open('Dataset/json_dataset/az_business.json', encoding="utf8"):
    json_object=json.loads(b)
    az_business[json_object["business_id"]]=[]


# In[4]:

reviews=[]
for r in open('Dataset/json_dataset/review.json', encoding="utf8"):
    json_object=json.loads(r)
    reviews.append(json_object)


# In[6]:

review_dict={}
az_business_review=[]
for r in reviews:
    if r["business_id"] in az_business:
        az_business[r["business_id"]].append(r["review_id"])
        az_business_review.append(r)
reviews=[]


# In[7]:

with open("Dataset/JSON_Dataset/az_review.json","w") as outfile:
    for r in az_business_review:
        json.dump(r,outfile)
        outfile.write("\n")

