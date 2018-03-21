import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn import linear_model
import matplotlib.pyplot as plt

clf = linear_model.LinearRegression()   # Classifier to be used

boston = datasets.load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)

# sns.pairplot(df)

# print(df.describe())
# print(pd.isnull(df).any())            # Check for NaN data

print(df.corr())

X = df['TAX'].values[:, np.newaxis]     # Feature data set
y = df['INDUS']                         # Label data set

classifier = clf.fit(X, y)

plt.scatter(X, y, color='b')
plt.plot(X, classifier.predict(X), color='r')

plt.show()
