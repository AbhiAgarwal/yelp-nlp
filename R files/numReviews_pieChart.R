user_10000 <- read.csv( file = "./yelp-user/user_improved_10000.csv")

grp1=subset(user_10000,numberOfReviews<2)
grp2=subset(subset(user_10000,numberOfReviews>2),numberOfReviews<=5)
grp3=subset(subset(user_10000,numberOfReviews>5),numberOfReviews<=10)
grp4=subset(subset(user_10000,numberOfReviews>10),numberOfReviews<=30)
grp5=subset(subset(user_10000,numberOfReviews>30),numberOfReviews<=50)
grp6=subset(subset(user_10000,numberOfReviews>50),numberOfReviews<=Inf)

slice<-c(length(grp1[,1])/length(user_10000[,1]),length(grp2[,1])/length(user_10000[,1]),length(grp3[,1])/length(user_10000[,1]),length(grp4[,1])/length(user_10000[,1]), length(grp5[,1])/length(user_10000[,1]),length(grp6[,1])/length(user_10000[,1]))*100

pie(slice,labels=paste(slice,'%',sep=''),main="Pie Chart")
