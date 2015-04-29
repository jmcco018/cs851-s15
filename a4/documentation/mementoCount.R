library(RColorBrewer)

data <- read.table("mementoCount")
allData = rep(data[,1])

title <- "Memento to URI"
pdf("mementoCount.pdf", height=4.0, width=4.5)

mp <- plot(allData, 1:length(allData), type="l", col="red", main=title, ylab="Population",xlab="Mementos")
