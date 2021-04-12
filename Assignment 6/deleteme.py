import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn import linear_model

# Set max display 
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# Read the tsv file 
df = pd.read_csv('C:/Users/DDY/Desktop/2021-Spring-textbooks/ADS-500B/Module6/airline_costs.csv',header=0)


# Check for linearity between dependent and independent variables

# Linearity between 'CustomersServed' and 'FlightLength'

# Correlation coefficient: 0.79 (strong)
      
plt.scatter(df['FlightLength'], df['CustomersServed'])
plt.title('CustomersServed Vs FlightLength', fontsize=14)
plt.xlabel('FlightLength', fontsize=14)
plt.ylabel('CustomersServed', fontsize=14)



# Linearity between 'CustomersServed' and 'DailyFlightTime'

# Correlation coefficient: 0.36 (weak) as we see outliers
      
plt.scatter(df['DailyFlightTime'], df['CustomersServed'])
plt.title('CustomersServed Vs DailyFlightTime', fontsize=14)
plt.xlabel('DailyFlightTime', fontsize=14)
plt.ylabel('CustomersServed', fontsize=14)


# =================== Detect and clean up outliers =====================


# Check outliers for 'FlightLength'
FlightLength_Q1 = df.FlightLength.quantile(0.25)
FlightLength_Q3 = df.FlightLength.quantile(0.75)
FlightLength_IQR = FlightLength_Q3 - FlightLength_Q1
FlightLength_out = (df.FlightLength < (FlightLength_Q1 - 1.5 * FlightLength_IQR)) | (df.FlightLength > (FlightLength_Q3 + 1.5 * FlightLength_IQR))

FlightLength_out # No outliers


DailyFlightTime_Q1 = df.DailyFlightTime.quantile(0.25)
DailyFlightTime_Q3 = df.DailyFlightTime.quantile(0.75)
DailyFlightTime_IQR = DailyFlightTime_Q3 - DailyFlightTime_Q1
DailyFlightTime_out = (df.DailyFlightTime < (DailyFlightTime_Q1 - 1.5 * DailyFlightTime_IQR)) | (df.DailyFlightTime > (DailyFlightTime_Q3 + 1.5 * DailyFlightTime_IQR))

DailyFlightTime_out # Outliers: row10,28,29


df = df[~(DailyFlightTime_out)] # Revove outliers from df

X = df[['FlightLength','DailyFlightTime']] 
y = df['CustomersServed']

#Split the data into train and test dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=42)

#Fitting Simple Linear regression data model to train data set
from sklearn.linear_model import LinearRegression
regressorObject=LinearRegression()
regressorObject.fit(X_train,y_train)

#predict the test set
y_pred_test_data=regressorObject.predict(X_test)

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressorObject.predict(X_train), color = 'blue')
plt.show()
