# -*- coding: latin-1 -*-

import csv
import json

reviewFile = './user_improved_1000.json'
csvFile = './user_improved_1000.csv'

reviewData = []
with open(reviewFile) as f:
    for line in f:
        reviewData.append(json.loads(line))
reviewData = reviewData[0]

f = csv.writer(open(csvFile, "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["average_stars", "fans", "number_of_friends", "numberOfReviews" "averageSentiment", "averageStars", "funnyVotes", "usefulVotes", "coolVotes"])

currentCount = 0
limit = 10000

for x in reviewData:
    if currentCount < limit:
        averageSentiment = 0
        averageStars = 0
        funnyVotes = 0
        usefulVotes = 0
        coolVotes = 0

        for i in x['userReviews']:
            averageSentiment += i['sentiment']
            averageStars += i['stars']
            funnyVotes += i['votes']['funny']
            coolVotes += i['votes']['cool']
            usefulVotes += i['votes']['useful']

        averageSentiment /= len(x['userReviews'])
        averageStars /= len(x['userReviews'])
        funnyVotes /= len(x['userReviews'])
        coolVotes /= len(x['userReviews'])
        usefulVotes /= len(x['userReviews'])
        numberOfReviews = len(x['userReviews'])

        f.writerow([unicode(x["average_stars"]).encode(("utf-8")),
                    unicode(x["fans"]).encode(("utf-8")),
                    unicode(x["number_of_friends"]).encode(("utf-8")),
                    unicode(numberOfReviews).encode(("utf-8")),
                    unicode(averageSentiment).encode(("utf-8")),
                    unicode(averageStars).encode(("utf-8")),
                    unicode(funnyVotes).encode(("utf-8")),
                    unicode(usefulVotes).encode(("utf-8")),
                    unicode(coolVotes).encode(("utf-8"))
                    ])
        currentCount += 1