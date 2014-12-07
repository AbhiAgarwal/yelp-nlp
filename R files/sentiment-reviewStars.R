review <- read.csv( file = "./yelp-NV/review.csv")

#correlation
sentiment_reviewStars <- cor( review$sentiment , review$review_stars)

#lm
lm.out = lm(review$sentiment ~ review$review_stars)
summary( lm.out)

plot(review$review_stars , review$sentiment)
abline(lm.out, col="red")