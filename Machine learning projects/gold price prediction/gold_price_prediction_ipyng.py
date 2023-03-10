# -*- coding: utf-8 -*-
"""gold price prediction.ipyng

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JPlloogHytsOEHHTMJA4JzPu4tgN-3GA

1-IMPORTING THE LIBRARIES
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

"""2-DATA COLLECTION AND PROCESSING"""

#loading the csv data to a pandasDataFrame
gold_data=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/project/gld_price_data (1).csv")

#to understand the data
#print first five rows
gold_data.head()

#print last five rows
gold_data.tail()

#number of rows and columns
gold_data.shape

#getting some basic information about data
gold_data.info()

#checking number of missing values
gold_data.isnull().sum()

#getting the statistical measures of data
gold_data.describe()

"""CORRELATION;
1. postive correlation
2. negative corr::elation
   









"""

correlation = gold_data.corr()

#constructing a heat map to understand the correlation
plt.figure(figsize = (8,8))
sns.heatmap(correlation, cbar=True, square=True, fmt=".1f", annot=True, annot_kws={"size":8})

#correlation values of GLD
print(correlation["GLD"])

#check the distribution of the gold price
sns.distplot(gold_data["GLD"],color="green")

"""splitting the  feature and target

"""

x = gold_data.drop(["Date","GLD",],axis=1)
y = gold_data["GLD"]

x_train, x_test, y_train, y_test =train_test_split(x, y, test_size = 0.2, random_state=2)

"""Model training:Random Forest Regressor,
               ,Descision Tree regressor
               Linear regressor





"""

x_train.head(3)

regressor = RandomForestRegressor()

#training the model
regressor.fit(x_train,y_train)

dt = DecisionTreeRegressor()
dt.fit(x_train,y_train)

lr = LinearRegression()
lr.fit(x_train,y_train)

"""Model Evaluation"""

#prediction on test data
test_data_prediction = regressor.predict(x_test)
test_data_prediction_dt = dt.predict(x_test)
test_data_prediction_lr = lr.predict(x_test)

# R2 score

r2_score_rf = metrics.r2_score(y_test, test_data_prediction)
print("R2 score Random forest: ", r2_score_rf)

r2_score_dt = metrics.r2_score(y_test, test_data_prediction_dt)
print("R2 score Dt: ", r2_score_dt)


r2_score_lr = metrics.r2_score(y_test, test_data_prediction_lr)
print("R2 score lr: ", r2_score_lr)

# best model here is Random_Forest

# hyper param tuning on RF

RandomForestRegressor()

params = {
    'n_estimators':[50,100,150,175],
     'max_depth': [1,2,3,4],
     'max_features':[1,2,3,4]

}

hyp = GridSearchCV(regressor,params,cv=10,scoring='r2')

hyp.fit(x_train,y_train)



hyp.best_params_

hyp.best_score_

regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

"""Model evaluation

"""

x_test.columns

x_test.sample(1).values

regressor.predict([[1360.030029,   79.32    ,   17.700001,    1.472299]])

"""Final Report:"""

print('R2_score',metrics.r2_score(y_test,y_pred))

