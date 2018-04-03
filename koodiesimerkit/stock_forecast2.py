import pandas as pd
import quandl
import math, datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

quandl.ApiConfig.api_key = 'iMS2CYmdLi5zXx5qAiAk' # use own api_key

# Get stock data
stock = 'EURONEXT/NOKIA'
df = quandl.get(stock, returns='pandas')      # Quandl has pandas dataframe built in

# print(df)

# Create dataframe
df = df[['Open', 'High', 'Low', 'Last', 'Volume', 'Turnover']]
df['VOL_PCT'] = (df['High'] - df['Low']) / df['Last'] * 100.0

df = df[['Open', 'Last', 'Volume', 'VOL_PCT']]

forecast_col = 'Last'

df.fillna(-99999, inplace=True)

pct = 0.05
forecast_out = int(math.ceil(pct*len(df)))      # pct of data set to where forecast is done in days

df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))  # Features, everything except label
X_lately = X[-forecast_out:]         # Time period to be forecasted 
X = X[:-forecast_out:]

df.dropna(inplace=True)             # Drop missing data

y = np.array(df['label'])           # Labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)    # Cross-validation

clf = LinearRegression(n_jobs=-1)   # Classifier to be used, n_jobs number of parallel jobs
clf.fit(X_train, y_train)           # Training

print()
last_date = df.iloc[-1].name
print("Last date:", last_date)

confidence = clf.score(X_test, y_test)      # Testing, result squared confidence
print("Confidence: ", round(confidence,4))

forecast_set = clf.predict(X_lately)        # Why not second parameter? - Label is known. (next day)
print("The next stock prices of" ,stock,"for", forecast_out, "days: ")

i = 0

# Console printing the forecast stock prices
while i < len(forecast_set):
    if i != 0:
        daily_diff_pct = round((forecast_set[i]-forecast_set[i-1])/(forecast_set[i-1]+forecast_set[i]/2)*100,3)
        daily_diff_lambda = lambda j: ("+" if j > 0 else "") + str(j)
        print("\t", str(np.round(forecast_set[i],3)), "\t", daily_diff_lambda(daily_diff_pct))
    else:
        print("\t", str(np.round(forecast_set[i],3)))
    i += 1

df['Forecast'] = np.nan     # Create empty array

# Populate the forecast set
for i in forecast_set:
    next_date = last_date + datetime.timedelta(days=1)
    df.loc[next_date] = [np.nan for j in range(len(df.columns)-1)] + [i] # [i] adds the item to the set
    last_date = next_date



# Plotting the results
df['Last'].plot()
df['Forecast'].plot()
plt.legend(loc=3)
plt.xlabel('Date')
plt.ylabel('Stock price')
plt.show()
