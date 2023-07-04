import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Step 1: Read earthquake data
data = pd.read_csv('earthquake.csv')

# Step 2: Feature extraction
# Assuming you have features 'magnitude', 'depth', and 'latitude'
features = ['Magnitude', 'Depth', 'Latitude']
target = 'Longitude'  # Assuming 'longitude' is the target variable

X = data[features]
y = data[target]

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Build and train the SVR model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Step 5: Make predictions on the test set
predictions = model.predict(X_test)

# Step 6: Evaluate the model
mse = mean_squared_error(y_test, predictions)
accuracy = 100 - np.sqrt(mse)  # Calculating accuracy as percentage

# Plotting accuracy
plt.figure(figsize=(8, 6))
plt.plot(range(len(y_test)), y_test, label='Actual')
plt.plot(range(len(predictions)), predictions, label='Predicted')
plt.xlabel('Data points')
plt.ylabel('Longitude')
plt.title(f"Predictive Model Accuracy: {accuracy:.2f}%")
plt.legend()
plt.show()
