
# coding: utf-8

# In[3]:


from textblob import TextBlob
text="I love the food and serving"
blob = TextBlob(text)
print (blob.sentiment.polarity)


# In[4]:


from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
extractor = ConllExtractor()
blob = TextBlob("Python is a high-level programming language.", np_extractor=extractor)
blob.noun_phrases
blob = TextBlob("Food was really good and serving was bad", np_extractor=extractor)
blob.noun_phrases


# In[5]:


from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob("Great place to hang out after work: the prices are decent, and the ambience is fun. It's a bit loud, but very lively. The staff is friendly, and the food is good. They have a good selection of drinks", analyzer=NaiveBayesAnalyzer(),np_extractor=extractor)
print (blob.sentiment)
blob.noun_phrases
print ("*********************************************")       
for i in blob.ngrams(n=2):
    str_text=""
    for j in i:
        str_text=str_text+j
        str_text+=" "
    text=TextBlob(str_text)
    if(text.sentiment.polarity>0):
        #print (text,"sentiment:",text.sentiment.polarity,"nouns:",text.noun_phrases)
        print(text)
print ("*********************************************") 
for i in blob.ngrams(n=3):
    str_text=""
    for j in i:
        str_text=str_text+j
        str_text+=" "
    text=TextBlob(str_text)
    if(text.sentiment.polarity>0):
        #print (text,"sentiment:",text.sentiment.polarity,"nouns:",text.noun_phrases)
        print(text)
print ("*********************************************")       
for i in blob.ngrams(n=4):
    str_text=""
    for j in i:
        str_text=str_text+j
        str_text+=" "
    text=TextBlob(str_text)
    if(text.sentiment.polarity>0):
        #print (text,"sentiment:",text.sentiment.polarity,"nouns:",text.noun_phrases)
        print(text)


# In[7]:


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
lines="Great place to hang out after work: the prices are decent, and the ambience is fun. It's a bit loud, but very lively. The staff is friendly, and the food is good. They have a good selection of drinks"
word_list = word_tokenize(lines)
#print (word_list)
filtered_words = [word for word in word_list if word not in stopwords.words('english')]
#print (filtered_words)
text=""
for i in filtered_words:
    text+=i
    text+=" "
print (text)
blob=TextBlob(text)

single_blob=[]
print ("*********************************************")
for i in blob.ngrams(n=1):
    str_text=""
    for j in i:
        str_text=str_text+j
        str_text+=" "
    text=TextBlob(str_text)
    if(text.sentiment.polarity>0):
        #print (text,"sentiment:",text.sentiment.polarity,"nouns:",text.noun_phrases)
        print(text)
        single_blob.append(str_text)
print ("*********************************************")
print (single_blob)
print ("*********************************************")

print ("*********************************************")
two_blob=[]
for i in blob.ngrams(n=2):
    str_text=""
    for j in i:
        str_text=str_text+j
        str_text+=" "
    text=TextBlob(str_text)
    if(text.sentiment.polarity>0):
        #print (text,"sentiment:",text.sentiment.polarity,"nouns:",text.noun_phrases)
        #print(text)
        
        two_blob.append(str_text)
print ("*********************************************")
print (two_blob)
print ("*********************************************")


# In[61]:


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
lines="Great place to hang out after work: the prices are decent, and the ambience is fun. It's a bit loud, but very lively. The staff is friendly, and the food is good. They have a good selection of drinks"
#lines="beautiful palace"
word_list = word_tokenize(lines)
filtered_words = [word for word in word_list if word not in stopwords.words('english')]
text=""
for i in filtered_words:
    text+=i
    text+=" "
#print (text)
blob=TextBlob(text)
traindata=[]
print ("*********************************************")
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
two_blob=[]
for i in blob.ngrams(n=2):
    str_text=""
    for j in i:
        str_text=str_text+j
        str_text+=" "
    text=TextBlob(str_text)
    text_tag=[]
    if(text.sentiment.polarity>0):
        #print (text,"sentiment:",text.sentiment.polarity,"nouns:",text.noun_phrases)
        #print(text)
        #print(text.noun_phrases)
        #text_tag=text.tags
        #text_word=word_tokenize(str_text)
        
        #print (text_tag)
        #for i in text_tag:
         #   print (i[0],":",i[1])
        two_blob.append(str_text)
print ("*********************************************")
#print (two_blob)
print (len(two_blob))
for i in two_blob:
    print (i)


# In[64]:


feature=[]
for i in two_blob:
    print (i)
    words=word_tokenize(i)
    for j in traindata:
        for k in words:
            if(j is not k):
                feature.append(k)
                break
print (len(feature))
print (feature)

