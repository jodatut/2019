
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

df_orig = pd.read_csv('Retail_Data.csv')


# In[3]:

df_orig.head(10)


# In[5]:

df = pd.get_dummies(df_orig, prefix='', prefix_sep='')


# In[6]:

df.head(10)


# In[7]:

df.drop('Trans_ID',axis=1,inplace=True)


# In[18]:

from mlxtend.frequent_patterns import apriori, association_rules

frequent_items = apriori(df, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_items, metric='lift', min_threshold=1)


# In[19]:

from scipy.cluster.hierarchy import dendrogram, linkage

dist = frequent_items.support

Z = linkage(dist, method='complete')


# In[20]:

from matplotlib import pyplot as plt

plt.figure()
dn = dendrogram(Z, labels=frequent_items.itemsets.tolist())
plt.xticks(rotation=90)


# In[ ]:



