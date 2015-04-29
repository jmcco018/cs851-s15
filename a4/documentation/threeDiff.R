library(RColorBrewer)

data <- read.table("sortedThreeDiff")
allData = rep(data[,1])

title <- "Three Word Jaccard Distance"
pdf("threeDiff.pdf", height=4.0, width=4.5)

mp <- plot(allData, 1:length(allData), type="l", col="red", main=title, ylab="Population",xlab="Jaccard Distance")
