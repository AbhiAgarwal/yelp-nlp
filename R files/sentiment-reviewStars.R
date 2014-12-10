#review <- read.csv( file = "./yelp-NV/review.csv")

#correlation
sentiment_reviewStars <- cor( review$sentiment , review$review_stars)

#lm
lm2.out = lm2(review$sentiment ~ review$review_stars)
summary( lm2.out)

plot(review$review_stars , review$sentiment)
abline(lm2.out, col="red")