library(zoo)

review <- read.csv( file = "./yelp-NV/review.csv")

# convert dates to YYYY-MM-DD
d <- review$yelping_since
lastday <- as.Date(as.yearmon(d, "%Y-%m"), frac = 1) #adds last day of month to date

numeric_dates <- as.numeric(lastday) # convert date to numeric (number of seconds since arbitrary date)

#lm
lm.out = lm(review$fans ~ numeric_dates)
#summary( lm.out)

plot(numeric_dates, review$fans, main="Plot", ylim = range (0,200), ylab = "Number of Reviews", xlab = "Member Since")
abline(lm.out, col="red")