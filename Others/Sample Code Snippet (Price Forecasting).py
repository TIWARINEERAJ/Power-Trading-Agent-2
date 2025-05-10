import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Dummy dataset
df = pd.read_csv('historical_power_prices.csv')

# Features
X = df[['hour', 'day_of_week', 'temp', 'wind_speed', 'solar_irradiance']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

preds = model.predict(X_test)