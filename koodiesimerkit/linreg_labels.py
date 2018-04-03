import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import cross_val_predict

import matplotlib.pyplot as plt

#df = pd.read_csv('http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2018-01-17/data/listings.csv.gz', 
#                   compression='gzip')
#
#df.to_csv('data.csv')

df = pd.read_csv('data.csv')

#print(df.info())

df = df[['host_response_time','host_response_rate','review_scores_rating']]

#print(df.head())
#print(df.host_response_time.unique())

df.host_response_rate = df.host_response_rate.str.strip('%')
df.host_response_rate = pd.to_numeric(df.host_response_rate)

#print(df.info())
#print(df.head())

#print(df.host_response_time.isnull().sum())

df = df.dropna()

# Encoding label encoder...
le = preprocessing.LabelEncoder()

cols = ['within an hour', 'within a day', 'a few days or more']

arr = le.fit_transform(df.host_response_time)

df.host_response_time = arr

# ...OR alternative way 
df_label = df.apply(preprocessing.LabelEncoder().fit_transform)

# Linear regression
lr = linear_model.LinearRegression()

y = df.review_scores_rating
X = df.drop(columns='review_scores_rating')

predict = cross_val_predict(lr, X, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predict, edgecolors=(0, 0, 0))
#ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

print(df.corr())