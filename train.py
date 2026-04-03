import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor # <-- NEW: Changed to Regressor
from sklearn.metrics import mean_absolute_error # <-- NEW: Change metric to MAE for regression
import pickle

# 1. Load the dataset
# As per our previous updates, ensure student_data.csv has the correct G1, G2, G3 columns
df = pd.read_csv('student_data.csv')

# 2. Select columns
# Features: historical data and behaviors
features = ['studytime', 'absences', 'G1', 'G2']
# Target: Continuous score, now a float for realism
target = 'G3'

X = df[features]
y = df[target]

# 3. Split data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the AI Model
print("Starting Real-Life AI Model Training...")
# <-- NEW: Using Regressor instead of Classifier for continuous output
model = RandomForestRegressor()
model.fit(X_train, y_train)

# --- NEW: Evaluation Metric for Regression ---
# Accuracy is not valid for regression. We use Mean Absolute Error.
# It tells you how many points, on average, the AI prediction is off from the true score.
print("Testing the AI on hidden data...")
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"📊 Model Realism Metric (Mean Absolute Error): {mae:.2f} points")
# For presentation, mention this: "Our predictions are typically off by only {mae:.2f} points."

# 5. Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Real-Life Model saved successfully as 'model.pkl'! 🎉")