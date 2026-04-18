import pandas as pd
import os

# -----------------------------
# 1. Check Current Directory
# -----------------------------
print("📁 Current Working Directory:", os.getcwd())

# -----------------------------
# 2. Load Dataset
# -----------------------------
file_path = os.path.join("Data", "employee_performance_data.csv")

if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ Dataset not found at: {file_path}")

df = pd.read_csv(file_path)

print("\n✅ Dataset Loaded Successfully!")
print(df.head())

# -----------------------------
# 3. Drop Unnecessary Column
# -----------------------------
if 'Employee_ID' in df.columns:
    df.drop('Employee_ID', axis=1, inplace=True)

# -----------------------------
# 4. Check Missing Values
# -----------------------------
print("\n🔍 Missing Values:\n", df.isnull().sum())

# (Optional) Handle missing values if needed
# df.fillna(method='ffill', inplace=True)

# -----------------------------
# 5. Convert Target Variable
# -----------------------------
df['Performance'] = df['Performance'].map({
    'Low': 0,
    'Medium': 1,
    'High': 2
})

# -----------------------------
# 6. Encode Categorical Features
# -----------------------------
categorical_cols = [
    'Gender',
    'Department',
    'Education_Level',
    'Job_Role',
    'Overtime'
]

df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

print("\n📊 After Encoding:\n")
print(df.head())

# -----------------------------
# 7. Save Processed Data
# -----------------------------
output_path = os.path.join("Data", "processed_data.csv")
df.to_csv(output_path, index=False)

print("\n✅ Processed dataset saved successfully!")
print("📁 Location:", output_path)