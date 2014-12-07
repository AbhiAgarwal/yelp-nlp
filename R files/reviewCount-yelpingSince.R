library(zoo)

review <- read.csv( file = "./yelp-NV/review.csv")

# convert dates to YYYY-MM-DD
d <- review$yelping_since
lastday <- as.Date(as.yearmon(d, "%Y-%m"), frac = 1) #adds last day of month to date

numeric_dates <- as.numeric(lastday) # convert date to numeric (number of seconds since arbitrary date)

#correlation
dates_vs_cou <- cor( numeric_dates , review$review_count)

#lm
lm.out = lm(review$review_count ~ numeric_dates)
#summary( lm.out)

plot(numeric_dates, review$review_count, main="Plot", ylim = range (0,3000), ylab = "Number of Reviews", xlab = "Member Since")
abline(lm.out, col="red")




