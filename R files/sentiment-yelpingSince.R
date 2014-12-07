library(zoo)

review <- read.csv( file = "./yelp-NV/review.csv")

#user_1000 <- read.csv( file = "./yelp-user/user_improved_1000.csv")


# convert dates to YYYY-MM-DD
d <- review$yelping_since
lastday <- as.Date(as.yearmon(d, "%Y-%m"), frac = 1) #adds last day of month to date

numeric_dates <- as.numeric(lastday) # convert date to numeric (number of seconds since arbitrary date)


model = lm(review$sentiment ~ numeric_dates)
plot(numeric_dates, review$sentiment, ylim = range( 0.15,0.25) )
abline(model, col="red")




