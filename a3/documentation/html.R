#data <- as.matrix(read.table("redirectsData",header=TRUE, sep=","))
data <- read.table("htmlwords",header=FALSE,sep=",")
barplot(as.matrix(data), main="HTML Words", beside=TRUE,col="blue",ylab="Word Frequency",xlab="Word Rank")
