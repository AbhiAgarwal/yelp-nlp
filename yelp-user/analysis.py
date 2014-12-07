# -*- coding: latin-1 -*-

import csv
import json
from textblob import TextBlob

def sentimentAnalysis(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

reviewFile = './user_10000.json'

reviewData = []
with open(reviewFile) as f:
    for line in f:
        reviewData.append(json.loads(line))

reviewData = reviewData[0]

reviewList = []
for i in reviewData.keys():
    reviewList.append(reviewData[i])

newList = []
for i in reviewList:
    newMap = {}

    newMap['average_stars'] = i['average_stars']
    newMap['fans'] = i['fans']
    newMap['number_of_friends'] = len(i['friends'])
    newMap['votes'] = i['votes']

    userReviews = i['userReviews']
    newMap['userReviews'] = []
    for x in userReviews:
        singleMap = {}
        singleMap['stars'] = x['stars']
        singleMap['votes'] = x['votes']
        singleMap['text'] = x['text']
        singleMap['sentiment'] = sentimentAnalysis(x['text'])
        newMap['userReviews'].append(singleMap)
    newList.append(newMap)

with open('./user_improved_10000.json', 'w') as outfile:
    json.dump(newList, outfile)