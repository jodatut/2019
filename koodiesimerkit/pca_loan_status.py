import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import Imputer
import warnings
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)


df = pd.read_csv("credit_train.csv")

def siivoaData(data, slice=1.0):

    # Mikä on muuttuja josta olemme kiinnostuneita?
    # Haluamme tietysti ymmärtää muuttujaa lainan tilanne "Loan staus"
    # Dikotominne muuttuja kuvaa sitä maksetaanko laina takaisin vai ei.

    #Haluammeko poistaa jotain muuttujia?
    poistettavatMuuttujat = ['Loan ID','Customer ID']
    data = data.drop(poistettavatMuuttujat, axis=1)

    #Annetaan keskiarvot puutuville tietopisteille
    sarakkeet =['Current Loan Amount','Credit Score','Annual Income','Years of Credit History',
            'Months since last delinquent','Number of Open Accounts','Number of Credit Problems',
           'Current Credit Balance','Maximum Open Credit','Bankruptcies','Tax Liens']
    muuttujanTäyttäjä = Imputer()
    data[sarakkeet] = muuttujanTäyttäjä.fit_transform(data[sarakkeet])
    data[sarakkeet] = data[sarakkeet].astype(int)

    #Poistetaan vielä NaN rivit
    data=data.dropna()

    #Note:  Discarding half of the data for testing purposes!
    index = int(len(data)*slice)
    data = data.loc[:index]


    #Valitaan muuttuja josta olemme kiinnostuneita ja koodataan se
    y = data['Loan Status']
    new_y = []
    for i in y:
        if i == 'Fully Paid':
            new_y.append(1)
        else:
            new_y.append(0)
    data = data.drop('Loan Status', axis=1)

    # Koodataan kategoriset muuttujat
    data = pd.get_dummies(data)
    #print(data.head())

    # Normalisoidaan data
    # Palautamme myös dataMean ja dataDev arvot jos haluamme syöttää koneelle uusia havaintoja
    dataMean = np.mean(data, axis=0)
    dataDev = np.std(data, axis=0)
    norm_x= (data - dataMean) / dataDev

    x = data.values #muutetaan numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    normMinMax = pd.DataFrame(x_scaled)

    return norm_x, normMinMax, data, new_y, dataMean, dataDev


xNorm, xMinMax, xNoNorm, y, xMean, xDev = siivoaData(df, slice=0.01)

print(xMinMax.head())

pca = PCA(n_components=43)
reducedX = pca.fit_transform(xMinMax)
print("Explained variance of 43 components:\n",pca.explained_variance_ratio_)

pca = PCA(n_components=2)
reducedX = pca.fit_transform(xMinMax)

colors = ['blue' if l==1 else 'red' for l in y]
for dp, c in zip(reducedX, colors):
    plt.scatter(dp[0], dp[1], color=c)
plt.show()


#Performing predictions with reduced dimensionality
xNorm, xMinMax, xNoNorm, y, xMean, xDev = siivoaData(df, slice=0.5)

for n_comp in [3, 10, 20, 43]:
    pca = PCA(n_components=n_comp)
    reducedX = pca.fit_transform(xMinMax)
    X_train, X_test, y_train, y_test = train_test_split(reducedX, y, test_size=0.33, random_state=42)

    clf = LogisticRegression().fit(X_train, y_train)
    score = accuracy_score(y_test, clf.predict(X_test))

    print('Accuracy with {} components: {}'.format(n_comp, score))




