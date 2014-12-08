#review <- read.csv( file = "../yelp-NV/review_1000.csv")

#correlation
sentiment_reviewStars <- cor( review$sentiment , review$review_stars)

#lm
lm.out = lm(review$sentiment ~ review$review_stars + review$usefulVotes + review$coolVotes)
summary( lm.out )

#plot(review$review_stars , review$sentiment)
#abline(lm.out, col="red")