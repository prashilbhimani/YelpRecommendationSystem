
import json
from langdetect import detect


reviews = []
for review in open('Dataset/JSON_Dataset/review.json', encoding="utf8"):
    reviews.append(json.loads(review))
print(len(reviews))


for review in reviews:
    if detect(review["text"]) != "en":
        reviews.remove(review)
print(len(reviews))




