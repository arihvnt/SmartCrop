# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1️⃣ Load your dataset
data = pd.read_csv("crdataset.csv")

# 2️⃣ Features & Labels
X = data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = data['label']  # column with crop names

# 3️⃣ Split into training & test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Save the model for later use
with open('crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as crop_model.pkl")
