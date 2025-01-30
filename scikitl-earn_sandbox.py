import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    'Size': [1400, 1600, 1700, 1875, 1100],  # Square feet
    'Bedrooms': [3, 4, 3, 3, 2],  # Number of bedrooms
    'Price': [300000, 400000, 350000, 450000, 200000]  # Price in USD
}

bedroom_df = pd.DataFrame(data)

X = bedroom_df.drop("Price", axis=1).values
y = bedroom_df["Price"].values


reg = LinearRegression()

reg.fit(X, y)

print(bedroom_df)

y_pred = reg.predict(X)

print(f"Predictions: {y_pred}")