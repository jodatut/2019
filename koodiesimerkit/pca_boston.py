from matplotlib import pyplot as plt
from sklearn.datasets import load_boston
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

dataset = load_boston()
df_boston = pd.DataFrame(dataset.data, columns=dataset.feature_names)
target = dataset.target
print(df_boston.head())

#Scale data
min_max_scaler = MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(df_boston.values)

#fit PCA with 13 components
pca = PCA(n_components=13)
reducedX = pca.fit_transform(x_scaled)

#Print information on target
print(max(target), min(target), sum(target)/len(target))

#Reformat target - from continuous to binary type
#0 if target<0 | 1 otherwise
average = sum(target)/len(target)
target = [0 if y<average else 1 for y in target]

colors = ['blue' if l==1 else 'red' for l in target]

for dp, c in zip(reducedX, colors):
    plt.scatter(dp[0], dp[1], color=c)
plt.show()



