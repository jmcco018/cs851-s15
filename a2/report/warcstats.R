#data <- as.matrix(read.table("redirectsData",header=TRUE, sep=","))
data <- read.table("warcstat",header=TRUE,sep=",")
barplot(as.matrix(data), main="Method", beside=TRUE,col="blue")
