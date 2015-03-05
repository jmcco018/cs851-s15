#data <- as.matrix(read.table("redirectsData",header=TRUE, sep=","))
data <- read.table("statdata",header=TRUE,sep=",")
barplot(as.matrix(data), main="Method", beside=TRUE,col=rainbow(2))
legend("topright",c("Mean","Median"),cex=0.6,bty="n",fill=rainbow(2));
