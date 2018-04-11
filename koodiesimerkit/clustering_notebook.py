
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

# Original source: https://www.datascience.com/blog/k-means-clustering
df = pd.read_csv('https://raw.githubusercontent.com/datascienceinc/learn-data-science/master/Introduction-to-K-means-Clustering/Data/data_1024.csv', delimiter='\t')


# In[3]:

df.head(10)


# In[8]:

from sklearn.utils import shuffle

df = shuffle(df)

df_train = df.iloc[:3000]
df_test = df.iloc[3000:]

df_train.shape


# In[11]:

from matplotlib import pyplot as plt

f1 = df_train.Distance_Feature.values
f2 = df_train.Speeding_Feature.values

X_train = np.array(list(zip(f1,f2)))

plt.scatter(f1,f2, c='black', s=7)


# In[15]:

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4).fit(X_train)

X_test = np.array(list(zip(df_test.Distance_Feature.values, df_test.Speeding_Feature)))

predict = kmeans.predict(X_test)

predict


# In[16]:

plt.scatter(X_test[:,0], X_test[:,1], c=predict)


# In[ ]:



