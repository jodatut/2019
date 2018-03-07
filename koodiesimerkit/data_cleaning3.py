import pandas as pd

# Used to plot the results
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

url = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'

# Use pandas to import data
orig_df = pd.read_csv(url)

# To keep original dataframe for referencing
df = orig_df.copy()

print(df.head())

print(df.dtypes)

# Convert object types
df['Transaction_date'] = pd.to_datetime(df['Transaction_date'])
df['Account_Created'] = pd.to_datetime(df['Account_Created'])
df['Last_Login'] = pd.to_datetime(df['Last_Login'])

print(df.dtypes)

# Convert prices to numeric in order to access math functions
df['Price'] = df['Price'].str.replace(',','')
df['Price'] = pd.to_numeric(df['Price'])

# Use general apply function
caps = lambda x: x.upper()
df['Country'] = df['Country'].apply(caps)

def test(x):
    if x == "Product1":
        return "P1"
    else:
        return x

df['Product'] = df['Product'].apply(test)

# New column to calculate logins within week
df['Login_week'] = ""

def lastweek(x):
    date = pd.Timestamp(2009, 2, 2)
    date_diff= pd.Timedelta(date-x).days
    if date_diff < 7:
        return "Last week"
    else:
        return "Not last week"
    
df['Login_week'] = df['Last_Login'].apply(lastweek)

# Select all rows with payment types
amex = df.loc[:,['Price','Payment_Type']]
amex = amex[amex['Payment_Type'] == 'Amex']
diners = df.loc[:,['Price','Payment_Type']]
diners = diners[diners['Payment_Type'] == 'Diners']
mc = df.loc[:,['Price','Payment_Type']]
mc = mc[mc['Payment_Type'] == 'Mastercard']
visa = df.loc[:,['Price','Payment_Type']]
visa = visa[visa['Payment_Type'] == 'Visa']

result = [amex, diners, mc, visa]
result_concat = pd.concat([amex, diners, mc, visa], keys={'amex': amex,
                                                          'diners': diners,
                                                          'mc': mc,
                                                          'visa': visa})

sum_amex = sum(amex['Price'])
sum_diners = sum(diners['Price'])
sum_mc = sum(mc['Price'])
sum_visa = sum(visa['Price'])

# Printing all purchases with each payment type
print("Sum of purchases with Amex is {}".format(sum_amex))
print("Sum of purchases with Diners is {}".format(sum_diners))
print("Sum of purchases with Mastercard is {}".format(sum_mc))
print("Sum of purchases with Visa is {}".format(sum_visa))

# Saving new dataframe to csv
result_concat.to_csv('result_dataframe.csv', encoding='utf8')

# Alternate way to get sum of payment types
payment_values = df['Payment_Type'].value_counts().to_frame()

# Plotting results

# Creating new dataframe to be plotted
df_plot = pd.DataFrame([[sum_amex, sum_diners, sum_mc, sum_visa]])
df_plot.columns = ['Amex', 'Diners', 'Mastercard', 'Visa']

df_plot.plot.bar()
plt.legend(loc=2)
plt.ylabel('Sum')
plt.show()
