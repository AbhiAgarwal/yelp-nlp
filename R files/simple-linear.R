review <- read.csv( file = "./yelp-NV/review.csv")

lm.out = lm(review$sentiment ~ review$review_stars)
summary( lm.out)

# linear plot
plot(review$review_stars , review$sentiment)
abline(lm.out, col="red")

# residual plot
lm.res = resid(lm.out)
plot(review$review_stars, lm.res)

# standard deviation check

means = aggregate(review$sentiment, list(review$review_stars), mean)
sds = aggregate(review$sentiment, list(review$review_stars), sd)
means_plus_sd <- means
means_minus_sd <- means
means_plus_sd$x = means_plus_sd$x + sds$x
means_minus_sd$x = means_minus_sd$x - sds$x
plot(means, ylim=c(-0.5,0.5))
points(means_plus_sd, col="blue")
points(means_minus_sd, col="blue")
abline(lm.out, col="red")
