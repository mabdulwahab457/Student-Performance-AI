import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score # <-- NEW: Tool to calculate accuracy
import pickle

# 1. Load the dataset
df = pd.read_csv('student_data.csv')

# 2. Select columns
features = ['studytime', 'absences', 'G1', 'G2']
target = 'G3'

X = df[features]
y = df[target]

# 3. Split data (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the AI Model
print("Starting AI Model Training...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

# --- NEW: Test the AI and calculate accuracy ---
print("Testing the AI on hidden data...")
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"📊 Final Model Accuracy: {accuracy * 100:.2f}%")
# -----------------------------------------------

# 5. Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully as 'model.pkl'! 🎉")