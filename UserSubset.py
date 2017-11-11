
# coding: utf-8

# In[3]:

import json


# In[5]:

az_reviews_dict={}
for r in open('Dataset/json_dataset/az_review.json', encoding="utf8"):
    json_object=json.loads(r)
    if json_object["user_id"] in az_reviews_dict:
        az_reviews_dict[json_object["user_id"]].append(json_object["review_id"])
    else:
        az_reviews_dict[json_object["user_id"]]=[json_object["review_id"]]


# In[7]:

users=[]
for u in open('Dataset/json_dataset/user.json', encoding="utf8"):
    json_object=json.loads(u)
    if json_object["user_id"] in az_reviews_dict:
        users.append(json_object)


# In[9]:

with open("Dataset/json_dataset/az_user.json","w") as outfile:
    for u in users:
        json.dump(u,outfile)
        outfile.write("\n")

