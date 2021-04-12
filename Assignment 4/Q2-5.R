library(ggplot2)
library(tidyverse)
library(ggpubr)


#Q2

#read the tsv file
custdata = read.table(file.choose(),header=T,sep='\t')
#print(summary(custdata))


#find highest y value
which.max(density(custdata$income)$y)

#use ggplot to plot density 
ggplot(custdata,aes(x=income))+geom_density(fill="darkgreen")+
  geom_vline(xintercept = density(custdata$income)$x[39])


#======================================

#Q3

#subset custdata to remove "NA" from "housing.type'
new_custdata = subset(custdata,housing.type != "NA")

#bar plot for "housing.type"
ggplot(new_custdata, aes(x=factor(housing.type)))+
  geom_bar(stat="count", width=0.7, fill="steelblue")+
  theme_minimal()

#======================================


#Q4

#subset the original to married and income of > $50000
Q4_custdata = subset(custdata,marital.stat == "Married" & income >50000)

#count the married and income of > $50000 who have insurance
ins_count_Q4 = sum(Q4_custdata$health.ins == "TRUE")
#count all the married and income of > $50000 
all_ins_count_Q4 = sum(Q4_custdata$health.ins == "TRUE") + 
                   sum(Q4_custdata$health.ins == "FALSE")
#calculate %
ins_pct_Q4 = (round(ins_count_Q4*100/ all_ins_count_Q4,2))
cat(ins_pct_Q4,"% of the customers who are married and have an income more 
      than $50,000 have insurance coverage.")


#count all who have insurance
ins_count_custdata = sum(custdata$health.ins == "TRUE")
#count all customers
all_ins_count_custdata = sum(custdata$health.ins == "TRUE") + 
                         sum(custdata$health.ins == "FALSE")
#calculate the %
ins_pct_count = round(ins_count_custdata*100 / all_ins_count_custdata,2)


cat(ins_pct_count,"% of all customers have insurance coverage.")



#==================================================

#Q5

#subset the original database to exclude the outliers and NA which are
#age < 0 and > 100; income < 0 and > 60000, NA for number of cars owned.
Q5_custdata = subset(custdata, subset=(custdata$age > 0) & (custdata$age < 100) &
  (custdata$income > 0) & (custdata$income < 600000) & (custdata$num.vehicles != "NA"))

#plot the corresponding scatter plot for all three variables using color-blind-friendly colors
plot(Q5_custdata$age,Q5_custdata$income,pch=19)
plot(Q5_custdata$age, Q5_custdata$num.vehicles, col = "#E69F00", pch = 19)
plot(Q5_custdata$income, Q5_custdata$num.vehicles, col = "#56B4E9", pch = 19)

#calculate their correlations and round to two decimal place
round(cor(Q5_custdata$age,Q5_custdata$income, method = c("pearson", "kendall", "spearman")),2)
round(cor(Q5_custdata$age,Q5_custdata$num.vehicles, method = c("pearson", "kendall", "spearman")),2)
round(cor(Q5_custdata$income,Q5_custdata$num.vehicles, method = c("pearson", "kendall", "spearman")),2)


