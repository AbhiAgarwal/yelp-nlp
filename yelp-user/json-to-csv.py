# -*- coding: latin-1 -*-

import csv
import json

reviewFile = './user_improved_10000.json'
csvFile = './user_improved_10000.csv'

reviewData = []
with open(reviewFile) as f:
    for line in f:
        reviewData.append(json.loads(line))
reviewData = reviewData[0]

f = csv.writer(open(csvFile, "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["average_stars", "fans", "number_of_friends", "userReviews"])

currentCount = 0
limit = 10000

for x in reviewData:
    if currentCount < limit:
        f.writerow([unicode(x["average_stars"]).encode(("utf-8")),
                    unicode(x["fans"]).encode(("utf-8")),
                    unicode(x["number_of_friends"]).encode(("utf-8")),
                    x['userReviews']])
        currentCount += 1