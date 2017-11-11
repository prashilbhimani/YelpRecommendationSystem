
# coding: utf-8

# In[2]:

import json


# In[3]:

business = []
for b in open('Dataset/json_dataset/business.json', encoding="utf8"):
    business.append(json.loads(b))


# In[4]:

az_business={}
business_list=[]
for b in business:
    if b["state"]=="AZ":
        az_business[b["business_id"]]=[]
        business_list.append(b)
business=[]


# In[ ]:

with open("Dataset/JSON_Dataset/az_business.json","w") as outfile:
    for r in az_business_review:
        json.dump(r,outfile)
        outfile.write("\n")

