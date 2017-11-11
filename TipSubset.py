
# coding: utf-8

# In[1]:

import json


# In[2]:

az_business = {}
for b in open('Dataset/json_dataset/az_business.json', encoding="utf8"):
    json_object=json.loads(b)
    az_business[json_object["business_id"]]=''


# In[3]:

az_user={}
for r in open('Dataset/json_dataset/az_user.json', encoding="utf8"):
    json_object=json.loads(r)
    az_user[json_object["user_id"]]=''


# In[4]:

tips=[]
tipped_users=[]
for t in open('Dataset/json_dataset/tip.json', encoding="utf8"):
    json_object=json.loads(t)
    if json_object["business_id"] in az_business:
        if json_object["user_id"] in az_user:
            tips.append(json_object)
        else:
            tipped_users.append(json_object["user_id"])
            tips.append(json_object)


# In[7]:

with open("Dataset/JSON_Dataset/az_tip.json","w") as outfile:
    for r in tips:
        json.dump(r,outfile)
        outfile.write("\n")


# In[8]:

new_users_dict={}
for t in tipped_users:
    new_users_dict[t]=''


# In[10]:

users=[]
for u in open('Dataset/json_dataset/user.json', encoding="utf8"):
    json_object=json.loads(u)
    if json_object["user_id"] in new_users_dict:
        users.append(json_object)


# In[12]:

with open("Dataset/JSON_Dataset/az_user.json","a") as outfile:
    for r in users:
        json.dump(r,outfile)
        outfile.write("\n")

