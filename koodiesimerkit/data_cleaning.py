import pandas as pd

orig_df = pd.read_csv('Tampereen_kaupungin_talousarvio_2014.csv')

# print(orig_df.head())
# print(orig_df.dtypes)
# print(orig_df.describe())

# Make copy for cleaning
df = orig_df.copy()

df.columns = df.columns.str.replace('\s+', '_')

# Drop rows with condition
df = df.drop(df[df.TY_hierarkia_taso_3 != 'Konsernihallinto'].index)

# Drop columns
df.drop(columns=['TY_hierarkia_taso_1', 'TY_hierarkia_taso_7'])

df['TA_2014'] = df['TA_2014'].str.replace('\xa0', '')
df['TA_2014'] = df['TA_2014'].str.partition(',')


print(df.describe())