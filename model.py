import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Data
# -----------------------------
df = pd.read_csv('Data/processed_data.csv')

print("Dataset Loaded ✅")

# -----------------------------
# 2. Split Features & Target
# -----------------------------
X = df.drop('Performance', axis=1)
y = df['Performance']

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 4. Train Model
# -----------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Model Trained ✅")

# -----------------------------
# 5. Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 6. Evaluation
# -----------------------------
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# -----------------------------
# 7. Feature Importance (ADD HERE)
# -----------------------------
importances = model.feature_importances_
features = X.columns

importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

print("\n🔥 Top 10 Important Features:\n")
print(importance_df.head(10))

# Plot
plt.figure()
plt.barh(importance_df['Feature'][:10], importance_df['Importance'][:10])
plt.title("Top 10 Features Affecting Employee Performance")
plt.gca().invert_yaxis()
plt.show()