# Q6.1

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Set max display 
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# Read the tsv file 
df = pd.read_csv('C:/Users/DDY/Desktop/2021-Spring-textbooks/ADS-500B/Module6/airline_costs.csv',header=0)

print (df)

# Check for nulls for preprocessing
print (df.isna().sum())

# Check for Multilinearity between 'DailyFlightTime' and 'FlightLength'
print (round(df['DailyFlightTime']. corr(df['FlightLength']),2))


# Check for linearity between dependent and independent variables

# Linearity between 'CustomersServed' and 'FlightLength'

print (round(df['CustomersServed']. corr(df['FlightLength']),2))
# Correlation coefficient: 0.79 (strong)
      
plt.scatter(df['FlightLength'], df['CustomersServed'])
plt.title('CustomersServed Vs FlightLength', fontsize=14)
plt.xlabel('FlightLength', fontsize=14)
plt.ylabel('CustomersServed', fontsize=14)
plt.show()


# Linearity between 'CustomersServed' and 'DailyFlightTime'

print (round(df['CustomersServed']. corr(df['DailyFlightTime']),2))
# Correlation coefficient: 0.36 (weak) as we see outliers
      
plt.scatter(df['DailyFlightTime'], df['CustomersServed'])
plt.title('CustomersServed Vs DailyFlightTime', fontsize=14)
plt.xlabel('DailyFlightTime', fontsize=14)
plt.ylabel('CustomersServed', fontsize=14)
plt.show()

# =================== Detect and clean up outliers =====================


# Check outliers for 'FlightLength'
FlightLength_Q1 = df.FlightLength.quantile(0.25)
FlightLength_Q3 = df.FlightLength.quantile(0.75)
FlightLength_IQR = FlightLength_Q3 - FlightLength_Q1
FlightLength_out = (df.FlightLength < (FlightLength_Q1 - 1.5 * FlightLength_IQR))|(df.FlightLength
                                                                                   > (FlightLength_Q3 + 1.5 * FlightLength_IQR))

print (FlightLength_out) # No outliers


DailyFlightTime_Q1 = df.DailyFlightTime.quantile(0.25)
DailyFlightTime_Q3 = df.DailyFlightTime.quantile(0.75)
DailyFlightTime_IQR = DailyFlightTime_Q3 - DailyFlightTime_Q1
DailyFlightTime_out = (df.DailyFlightTime < (DailyFlightTime_Q1 - 1.5 * DailyFlightTime_IQR))|(df.DailyFlightTime
                                                                                               > (DailyFlightTime_Q3 + 1.5 * DailyFlightTime_IQR))

print(DailyFlightTime_out) # Outliers: row10,28,29


df = df[~(DailyFlightTime_out)] # Revove outliers from df


# Perform Multiple Linear Regression using statsmodels

X = df[['FlightLength','DailyFlightTime']] 
y = df['CustomersServed']

X = sm.add_constant(X) # adding a constant
 
model = sm.OLS(y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

# Equation: CustomersServed = 179.69 * FlightLength - 244.11 * DailyFlightTime - 7372.77
# R-squared = 0.654


# ========================== Second linear regression model ========================

# Linearity between 'CustomersServed' and 'FlightLength'

print (round(df['TotalAssets']. corr(df['CustomersServed']),2))
# Correlation coefficient: 0.89 (strong)
      
plt.scatter(df['CustomersServed'], df['TotalAssets'])
plt.title('TotalAssets Vs CustomersServed', fontsize=14)
plt.xlabel('TotalAssets', fontsize=14)
plt.ylabel('CustomersServed', fontsize=14)
plt.show()


# Check outliers for 'CustomersServed'
CustomersServed_Q1 = df.CustomersServed.quantile(0.25)
CustomersServed_Q3 = df.CustomersServed.quantile(0.75)
CustomersServed_IQR = CustomersServed_Q3 - CustomersServed_Q1
CustomersServed_out = (df.CustomersServed
                       < (CustomersServed_Q1 - 1.5 * CustomersServed_IQR)) | (df.CustomersServed
                                                                              > (CustomersServed_Q3 + 1.5 * CustomersServed_IQR))
 
print (CustomersServed_out) # Outliers: row1,24,25

df = df[~(CustomersServed_out)] # Revove outliers from df

# Perform Multiple Linear Regression

x = df[['CustomersServed']] 
y = df['TotalAssets']

x = sm.add_constant(x) # adding a constant
 
model = sm.OLS(y, x).fit()
predictions = model.predict(x) 
 
print_model = model.summary()
print(print_model)

# Equation: TotalAssets = 0.0072 * CustomersServed + 2.86
# R-squared = 0.472
