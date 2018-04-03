import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import cross_val_predict

import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df = df[['review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','review_scores_rating']]

#print(df.isnull().sum())

# Drop rows where all are nan
df.dropna(axis=0, how='all', inplace=True)

print(df.isnull().sum())

# Impute median value for original missing values and generate new dataframe
imputer = preprocessing.Imputer(strategy='median')
df_imp = pd.DataFrame(imputer.fit_transform(df))
df_imp.columns = df.columns
df_imp.index = df.index

print(df_imp.isnull().sum())

lr = linear_model.LinearRegression()

y = df_imp.review_scores_rating
X = df_imp.drop(columns='review_scores_rating')

predict = cross_val_predict(lr, X, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predict, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

corr = df_imp.corr()
