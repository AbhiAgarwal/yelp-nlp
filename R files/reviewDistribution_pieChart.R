user_10000 <- read.csv( file = "../yelp-user/user_improved_10000.csv")
sorted_user = sort(user_10000$numberOfReviews, decreasing = TRUE)
grp1=sorted_user[1:100]
grp2=sorted_user[101:500]
grp3=sorted_user[501:1000]
grp4=sorted_user[1001:2000]
grp5=sorted_user[2001:9993]
labels <- c("Top 1", "Next 4", "Next 5", "Next 10", "Next 80")
pie(c(sum(grp1),sum(grp2),sum(grp3),sum(grp4),sum(grp5)), labels = paste(labels, '%', sep =''))