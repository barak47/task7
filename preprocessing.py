import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('raw_data.csv')
df.fillna(df.mean(), inplace=True)
scaler = StandardScaler()
df[['Temperature', 'Wind Speed']] = scaler.fit_transform(df[['Temperature', 'Wind Speed']])
df.to_csv('processed_data.csv', index=False)
