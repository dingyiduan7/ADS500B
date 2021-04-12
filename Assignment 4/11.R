#Q5.2

library(RMySQL)
library(ggplot2)

# Set the connection parameters
connection <- dbConnect(dbDriver("MySQL"), user = "root", password = "FLZX3QCysyhl9t!!", dbname = "auto")


# Check the connection
dbListTables(connection)

# Obtain the table "mpg"
table = dbSendQuery(connection, 'SELECT * from mpg')

# Store the table
table = fetch(table, n= -1)
# View the table
View(table)


# Obtain correlation coefficient, round it to two decimal place
round(cor(table$horsepower, table$weight, method = c("pearson", "kendall", "spearman")),2)

#plot the variables and show regression line
ggplot(table, aes(x=horsepower,y=weight, color=mpg)) + geom_point()

#generate a random number seed and then use the kmeans function.
set.seed(100)
tableCluster = kmeans(table[, 4:5], 3, nstart = 50)

table(tableCluster$cluster, table$mpg)

#plot the new cluster data
ggplot(table, aes(x=horsepower,y=weight,color=tableCluster$cluster)) + geom_point()


# Close the connection
#dbDisconnect(connection)
