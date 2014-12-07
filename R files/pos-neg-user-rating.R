user_1000 <- read.csv( file = "./yelp-user/user_improved_1000.csv")
user_10000 <- read.csv( file = "./yelp-user/user_improved_10000.csv")

review_1000 <- read.csv( file = "./yelp-NV/review_1000.csv")

depressed_subset <- subset(user_10000, averageSentiment < 0)
happy_subset <- subset(user_10000, averageSentiment > 0)

happy.stars <- hist(happy_subset$average_stars)
depressed.stars <- hist(depressed_subset$average_stars)

plot (happy.stars, col=rgb(0,0,1,1/4), xlim=c(0,5), xlab = "Average Rating", main = "avg rating freq for positive & negative users")
plot( depressed.stars, col=rgb(1,0,0,1/4), xlim=c(0,5), add = T)