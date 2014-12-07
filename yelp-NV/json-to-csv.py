# -*- coding: latin-1 -*-

import csv
import json

stateNeeded = 'NV'
reviewFile = './yelp-' + stateNeeded + '/review.json'
csvFile = './yelp-' + stateNeeded + '/review_10000.csv'

reviewData = []
with open(reviewFile) as f:
    for line in f:
        reviewData.append(json.loads(line))
reviewData = reviewData[0]

f = csv.writer(open(csvFile, "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["latitude", "longitude", "stars", "review_stars", "text", "sentiment", "review_count", "average_stars", "yelping_since", "fans", "funnyVotes", "usefulVotes", "coolVotes"])

currentCount = 0
limit = 10000

for x in reviewData:
    if currentCount < limit:
        funnyVotes = x["votes"]["funny"]
        usefulVotes = x["votes"]["useful"]
        coolVotes =  x["votes"]["cool"]
        f.writerow([unicode(x["latitude"]).encode(("utf-8")),
                    unicode(x["longitude"]).encode(("utf-8")),
                    unicode(x["stars"]).encode(("utf-8")),
                    unicode(x["review_stars"]).encode(("utf-8")),
                    unicode(x["text"]).encode(("utf-8")),
                    unicode(x["sentiment"]).encode(("utf-8")),
                    unicode(x["review_count"]).encode(("utf-8")),
                    unicode(x["average_stars"]).encode(("utf-8")),
                    unicode(x["yelping_since"]).encode(("utf-8")),
                    unicode(x["fans"]).encode(("utf-8")),
                    unicode(funnyVotes).encode(("utf-8")),
                    unicode(usefulVotes).encode(("utf-8")),
                    unicode(coolVotes).encode(("utf-8"))])
        currentCount += 1