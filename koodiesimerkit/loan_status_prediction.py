import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.svm import SVC
import warnings
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
    mid_point = int(len(data)*slice)
    data = data.loc[:mid_point]


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

xNorm, xMinMax, xNoNorm, y, xMean, xDev = siivoaData(df, slice=0.25)

cases = []

for x in [xNorm, xMinMax, xNoNorm]:
    case = {}
    case['x_train'], case['x_test'], case['y_train'], case['y_test'] = train_test_split(x, y, test_size= 0.25, random_state=33)
    cases.append(case)

classifiers = [SGDClassifier(), LogisticRegression(), SVC()]

for i, case in enumerate(cases):
    print("Evaluating the models with data from the case #{}".format(i+1))
    for j, clf in enumerate(classifiers):
        #train model with train data
        clf.fit(X=case['x_train'], y=case['y_train'])
        #predict test data
        predictions = clf.predict(X=case['x_test'])
        #calculate the accuracy
        accuracy = accuracy_score(case['y_test'], predictions)

        print("\t Classifier #{} achieved {} accuracy on test data.".format(j+1, accuracy))


# Implement Cross Validation using Logistic Regression classifier
# Using MinMax Normalized data given it performed better
print("Running Cross-Validation using Logistic Regression classifier \n"
    +"and MinMax-Normalized data given it performed better...")
clf = LogisticRegression()
# Use all data available (slice=1.0):
xNorm, xMinMax, xNoNorm, y, xMean, xDev = siivoaData(df, slice=1.0)
# 5 fold cross validation
scores = cross_val_score(clf, xMinMax, y, verbose=1, cv=5)

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



