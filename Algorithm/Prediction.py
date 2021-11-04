import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data=pd.read_csv("F:\Sample bootstrap\indian_crime_list.csv")

data_years = data.drop(["Crime Head"], axis=1)
data_years = data_years.drop(["2016"], axis=1)

data_years.corr()

# Importing the dataset

X = data_years.iloc[:, :-1].values
y = data_years.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

a = 0
for i in y_pred:
    a = a + i


population = 1350000000
per_lakh = 100000
average = (a/population)*per_lakh

print("Prediction", average)




