# Q6.2

library(cluster)
library(factoextra)


# Read the file
lpga = read.table('C:/Users/DDY/Desktop/2021-Spring-textbooks/ADS-500B/Module6/
                  lpga2008.csv',header=T,sep=',')

# Remove '?' and '0's
lpga[lpga == '?' && '0'] = NA
lpga = na.omit(lpga)

# Count nulls >>> no nulls
sum(is.na(lpga))


# Standardizing the dataset
#lpga_golfer = lpga[,1, drop=FALSE]
lpga_st = scale(lpga[,2:ncol(lpga)])
lpga_st = as.data.frame(lpga_st)

#lpga_st <-cbind(lpga_golfer,lpga_st)

# Determining 'k'

# Using nbClust() to determine 'k' value
NbClust(lpga_st,distance='euclidean', method='kmeans') # According to majority rule,
# the best number of clusters is 2


# ===================== Agglomerative (Agnes) clustering =================

# Build the clusters in the Agglomerative method using the agnes() function
aclusters = agnes(lpga_st,metric = 'euclidean',stand=FALSE)

# Agglomerative coefficient
aclusters$ac

# Ploting Agnes Dedogram
pltree(aclusters, cex=0.6, hang=-1, main = 'Dendrogram of Agnes')

# Indicating rectangles on the plot to visualize 2 clusters
rect.hclust(aclusters, k=2, border = 2:5)

# Grouping clusters using cutree() function
grp_agnes = cutree(aclusters, k=2)

# Forming table to see the cluster size
table(grp_agnes)

# Visualization using fviz_cluster
fviz_cluster(list(data=lpga_st,cluster=grp_agnes))


# ===================== Divisive (Diana) clustering =================

# Build the clusters in the Divisive method using the diana() function
diclusters = diana(lpga_st,metric = 'euclidean',stand=FALSE)

# Divisive coefficient
diclusters$dc

# Ploting Diana Dedogram
pltree(diclusters, cex=0.6, hang=-1, main = 'Dendrogram of Diana')

# Indicating rectangles on the plot to visualize 2 clusters
rect.hclust(diclusters, k=2, border = 3:5)

# Grouping clusters using cutree() function
grp_diana = cutree(diclusters, k=2)

# Forming table to see the cluster size
table(grp_diana)

# Visualization using fviz_cluster
fviz_cluster(list(data=lpga_st,cluster=grp_diana))