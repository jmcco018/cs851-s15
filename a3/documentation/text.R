#data <- as.matrix(read.table("redirectsData",header=TRUE, sep=","))
data <- read.table("textwords",header=FALSE,sep=",")
barplot(as.matrix(data), main="Text Words", beside=TRUE,col="blue",ylab="Word Frequency",xlab="Word Rank")
