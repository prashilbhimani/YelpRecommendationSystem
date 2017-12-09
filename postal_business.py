
# coding: utf-8

# In[2]:


import json
business=[]
for i in open('az_business.json', encoding="utf8"):
    business.append(json.loads(i))


# In[14]:


postal_business={}
for i in business:
    if i["postal_code"] in postal_business:
        postal_business[i["postal_code"]].append(i["business_id"])
    else:
        postal_business[i["postal_code"]]=[i["business_id"]]


# In[18]:


with open("postal_business.json","w") as outfile:
    json.dump(postal_business,outfile)
    outfile.write("\n")

