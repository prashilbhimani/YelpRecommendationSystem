import json
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
import nltk


# In[2]:

business = []
for b in open('Dataset/az_business_review.json', encoding="utf8"):
    business=json.loads(b)


# In[3]:

def filteredWords(text):
    text=TextBlob(text)
    word_list = word_tokenize(str(text))
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    text = ' '.join(filtered_words)
    return text


# In[4]:

def getNGram(text,n,polarity):
    key_words=[]
    text=TextBlob(text)
    for word in text.ngrams(n):
        word = ' '.join(word)
        wordBlob=TextBlob(word)
        if wordBlob.sentiment.polarity>0.5 and polarity>0.2:
            if str(wordBlob) not in key_words:
                key_words.append(str(wordBlob))
        if wordBlob.sentiment.polarity<-0.5 and polarity<-0.2:
            if str(wordBlob) not in key_words:
                key_words.append(str(wordBlob))
    return key_words
    


# In[5]:

def getNouns(text):
    nouns=[]
    for word,pos in nltk.pos_tag(nltk.word_tokenize(text)):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)
    return nouns                  


# In[6]:

def getAdjectives(text):
    adjectives=[]
    for word,pos in nltk.pos_tag(nltk.word_tokenize(text)):
         if (pos == 'JJ' or pos == 'JJR' or pos == 'JJS'):
             adjectives.append(word)
    return adjectives                 


# In[10]:

all_key_words={}
business_keys=list(business.keys())
for b in business_keys[45000:]:
    all_key_words[b]={}
    for r in business[b]:
        #print(r)
        review=r.lower().split(".")
        for r in review:
            text=TextBlob(r)
            polarity=text.sentiment.polarity
            #text1=filteredWords(r)
            text1=r
            nouns=getNouns(text1)
            adjectives=getAdjectives(text1)
            #print(text1)
            #print("noun ",end="")
            #print(nouns)

            #print("adjectives ",end="")
            #print(adjectives)

            #one_grams=getNGram(filteredWords(text1),1,polarity)
            two_grams=getNGram(filteredWords(text1),2,polarity)
            #print(two_grams)
            
            for k in two_grams:
                k=k.split(" ")
                if (k[0] in nouns and k[1] in adjectives):
                    if k[0] in all_key_words[b].keys():
                        all_key_words[b][k[0]].append(k[1])
                    else:
                        all_key_words[b][k[0]]=[k[1]]

                if (k[1] in nouns and k[0] in adjectives):
                    if k[1] in all_key_words[b].keys():
                        all_key_words[b][k[1]].append(k[0])
                    else:
                        all_key_words[b][k[1]]=[k[0]]
    #for k in final_keywords.keys():
    #    print(k,end=" ")
    #    print(len(final_keywords[k]))
    #for k in sorted(all_key_words[b], key=lambda k: len(all_key_words[b][k]), reverse=True):
    #    print(k,end=" ")
    #    print(final_keywords[k])
    #print(" ")
    print(len(all_key_words[b]), end=" ")
    print(len(business[b]))
    with open("Dataset/az_business_tags2.json","a") as outfile:
        temp={}
        temp['business_id']=b
        temp['tags']=all_key_words[b]
        json.dump(temp,outfile)
        outfile.write("\n")
