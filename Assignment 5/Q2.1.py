# Q2.1

import pymysql.cursors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Importing Statsmodels.api library from Stamodel package
import statsmodels.api as sm
# Import library to produce a 3D plot
from mpl_toolkits.mplot3d import Axes3D
from sklearn import linear_model


# Connect to the database
connection = pymysql.connect(host='localhost',
user='root',
password='FLZX3QCysyhl9t!!',
db='auto',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM mpg'
        cursor.execute(sql)
# Extract the data in a dataframe
        df = pd.DataFrame(cursor.fetchall())
finally:
        connection.close()

print (df)

# Calculate correlation between mpg and other variables
# "weight" has the highest correlation with "mpg", so we decide to use it as X
        #for y = mX + c formula
corrMatrix = df.corr()
print(corrMatrix.mpg)
print()


# ============================================Simple linear regression model

# Creating X and Y
#X = df.weight
#Y = df.mpg

# Adding a constant to get an intercept
#X_sm = sm.add_constant(X)


# Fitting the resgression line using 'OLS'
#SLR = sm.OLS(Y, X_sm).fit()


# Performing a summary to list out all the different parameters of the regression line fitted
#print(SLR.summary())


# Equation: y = -0.0076 * weight + 46.2287
# R-squared = 0.691

# Visualizing the regression line
#plt.scatter(X, Y)
#plt.plot(X, -0.0076 * X + 46.2287, 'r')
#plt.title('mpg vs. weight')
#plt.xlabel('weight')
#plt.ylabel('mpg')
#plt.show()

# ============================================Simple linear regression model

#Create another models using two varibales: weight and displacement

df.weight = df.weight.values.reshape(-1,1)
df.displacement = df.displacement.values.reshape(-1,1)
X = df[['weight','displacement']]
Y = df.mpg

# Adding a constant
X_sm = sm.add_constant(X) 

# Fitting the resgression line using 'OLS'
MLR = sm.OLS(Y, X_sm).fit()
print(MLR.summary())


# Equation: y = -0.0058 * weight - 0.0164 * displacement + 43.8052
# R-squared = 0.698


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1 = df['weight']
x2 = df['displacement']
ax.scatter(x1, x2, Y, c='r', marker='o')
# Set axis labels
ax.set_xlabel('weight')
ax.set_ylabel('displacement')
ax.set_zlabel('mpg')
plt.show()










































