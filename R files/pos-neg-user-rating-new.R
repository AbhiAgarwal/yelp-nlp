user_10000 <- read.csv( file = "./yelp-user/user_improved_10000.csv")

depressed_subset <- subset(user_10000, averageSentiment < 0)
happy_subset <- subset(user_10000, averageSentiment > 0)

happy.stars <- hist(happy_subset$average_stars)
depressed.stars <- hist(depressed_subset$average_stars)

d <- depressed.stars$counts/nrow(depressed_subset)
h <- happy.stars$counts/nrow(happy_subset)

barplot(d,col=rgb(1,0,0,1/4), xlab = "Star Rating", ylab = "Weighted Freq", main = "Star Rating Frequency for Pos & Neg Users")
barplot(h,col=rgb(0,0,1,1/4), add = T)

legend("top", 
       legend = c("Positive", "Negative"), 
       fill = c("blue", "red"))