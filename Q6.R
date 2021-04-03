library(ggplot2)
library(tidyverse)
library(ggpubr)
library(datasets)
library(factoextra)

#Q6

#read the file
dating = read.table(file.choose(),header=T,sep=',')


#calculate the correlation coefficients
round(cor(dating$Icecream,dating$Games, method = c("pearson", "kendall", "spearman")),2)
round(cor(dating$Miles, dating$Games, method = c("pearson", "kendall", "spearman")),2)


#plot the variables and show regression line
ggplot(dating, aes(x=Miles,y=Games)) + geom_point() + stat_smooth(method='lm')

#calculate the coefficient for the predictor(Miles) and intercept.
lm(Games ~ Miles, dating)

#linear equation: Games = 0.00009003 * Miles + 3.532



# Plot variables and color points using "Like"
ggplot(dating, aes(x=Miles,y=Games,color=Like)) + geom_point()


#generate a random number seed and then use the kmeans function.
set.seed(100)
datingCluster = kmeans(dating[, 1:2], 3, nstart = 50)

table(datingCluster$cluster, dating$Like)

#plot the new cluster data
ggplot(dating, aes(x=Miles,y=Games,color=datingCluster$cluster)) + geom_point()
