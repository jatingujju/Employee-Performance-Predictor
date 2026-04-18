import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
df = pd.read_csv('Data/processed_data.csv')

print("Dataset Loaded ✅")
print(df.head())

# -----------------------------
# 1. Distribution of Performance
# -----------------------------
sns.countplot(x='Performance_High', data=df)
plt.title("High Performance Count")
plt.show()

# -----------------------------
# 2. Correlation Heatmap
# -----------------------------
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# -----------------------------
# 3. Experience vs Performance
# -----------------------------
sns.boxplot(x='Performance_High', y='Years_Experience', data=df)
plt.title("Experience vs Performance")
plt.show()

# -----------------------------
# 4. Training Hours vs Performance
# -----------------------------
sns.boxplot(x='Performance_High', y='Training_Hours', data=df)
plt.title("Training vs Performance")
plt.show()