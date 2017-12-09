
# coding: utf-8

# In[29]:


import json
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
import nltk

user_business = {}
for b in open('az_review.json', encoding="utf8"):
    business=json.loads(b)
    user_business[business["user_id"]]=[]


# In[32]:


for b in open('az_review.json', encoding="utf8"):
    business=json.loads(b)
    if int(business["stars"])>3:
        user_business[business["user_id"]].append(business["business_id"]);


# In[47]:


with open("user_business_gt3.json","w") as outfile:
    json.dump(user_business,outfile)
    outfile.write("\n")
        

