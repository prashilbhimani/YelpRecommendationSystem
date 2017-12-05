
# coding: utf-8

# In[5]:


import json
business = []
for b in open('az_review.json', encoding="utf8"):
    business.append(json.loads(b))


# In[24]:


review=[]
j=0
for i in business:
    print (i['text'])
    review.append(i['text'])
    j+=1
    if(j>3):
        break


# In[34]:


from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
traindata=[]
for i in review:
    #print (i)
    #print ("********************")
    text=TextBlob(i)
    print (text.sentiment.polarity)
    print ("*********************************************")
    if(text.sentiment.polarity>0):
        word_list = word_tokenize(i)
        filtered_words = [word for word in word_list if word not in stopwords.words('english')]
        text=""
        for i in filtered_words:
            text+=i
            text+=" "
        #print (text)
        blob=TextBlob(text)
        for i in blob.ngrams(n=1):
            str_text=""
            for j in i:
                str_text=str_text+j
                str_text+=" "
            text=TextBlob(str_text)
            if(text.sentiment.polarity>0):
                #print (text,"sentiment:",text.sentiment.polarity,"nouns:",text.noun_phrases)
                #print(text)
                if str_text not in traindata:
                    traindata.append(str_text)
        print (traindata)
    print ("*********************************************")
print ("######################################")    
print (traindata)

