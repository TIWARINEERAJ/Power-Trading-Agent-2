import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

class PriceForecaster:
    def __init__(self):
        self.model = RandomForestRegressor()

    def prepare_data(self, df):
        df['hour'] = pd.to_datetime(df['Time']).dt.hour
        X = df[['hour', 'Demand', 'Supply']]
        y = df['Price']
        return train_test_split(X, y, test_size=0.2)

    def train(self, df):
        X_train, X_test, y_train, y_test = self.prepare_data(df)
        self.model.fit(X_train, y_train)
        preds = self.model.predict(X_test)
        print("MAE:", mean_absolute_error(y_test, preds))
        os.makedirs("models", exist_ok=True)
        joblib.dump(self.model, "models/price_model.pkl")

    def predict(self, X):
        return self.model.predict(X)