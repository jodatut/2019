
# Get a local copy of the dataset
# https://www.ibm.com/communities/analytics/watson-analytics-blog/guide-to-sample-datasets/

import pandas as pd

# See https://matplotlib.org/faq/usage_faq.html#interactive-example
# Might be only related MacOS
import matplotlib.pyplot as plt
plt.ion()
# plt.plot([1.6, 2.7])

# Using Customer Support data here
df = pd.read_csv('data/01-source/WA_Fn-UseC_-Telco-Customer-Churn.csv')

print(df.columns)
print(df.shape)
print(df.head(20))
print(df.describe())

from pandas.plotting import scatter_matrix
#  %matplotlib inline

scatter_matrix(df, figsize=[2,2], )
