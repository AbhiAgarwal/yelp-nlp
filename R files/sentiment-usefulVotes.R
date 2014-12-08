review_1000 <- read.csv( file = "./yelp-NV/review_1000.csv")

lm.out <- lm(review_1000$usefulVotes ~ review_1000$sentiment)

plot(review_1000$sentiment, review_1000$usefulVotes, ylim = c(0,10))
abline(lm.out, col = "red")