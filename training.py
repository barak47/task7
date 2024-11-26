import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('processed_data.csv')
X = df[['Humidity', 'Wind Speed']]
y = df['Temperature']

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
