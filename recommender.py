
# coding: utf-8

# In[1]:


from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# In[4]:


print (fuzz.ratio("How are you?", "How are you?"))
print (fuzz.ratio("How are you?", "Who are you?"))


# In[5]:


from fuzzywuzzy import process
choices = ['HI', 'HELLO', 'HEY', 'GOOD MORNING','TELL ME A JOKE', 'JOKE', 'FUNNY','GIVE ME A TIP', 'TIP', 'LESSON','WHAT IS YOUR NAME', 'WHO ARE YOU', 'HOW ARE YOU?']


# In[10]:


process.extractOne("whoe are you?", choices)


# In[7]:


test=["Hello","morning","joke","funny"]


# In[11]:


business_tags=['atmosphere','food', 'service','place','hour','staff','music']
U1=['atmosphere','burger']
U2=['service']
U3=['hour']
U4=['dance']


# In[22]:


c1=[]
c1.append("b1")
for i in U1:
    tup=process.extractOne(str(i),business_tags)
    if tup[1]>=80:
        c1.append("U1")        
for i in U2:
    tup=process.extractOne(str(i),business_tags)
    if tup[1]>=80:
        c1.append("U2")        
for i in U3:
    tup=process.extractOne(str(i),business_tags)
    if tup[1]>=80:
        c1.append("U3")        
for i in U4:
    tup=process.extractOne(str(i),business_tags)
    if tup[1]>=80:
        c1.append("U4")
print (len(c1))
print (c1)

