import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv('Data/processed_data.csv')

X = df.drop('Performance', axis=1)
y = df['Performance']

# -----------------------------
# 2. Train Model
# -----------------------------
model = RandomForestClassifier()
model.fit(X, y)

# -----------------------------
# 3. UI
# -----------------------------
st.title("🚀 Employee Performance Predictor")

st.write("Enter employee details to predict performance")

# -----------------------------
# 4. Input Fields
# -----------------------------
age = st.slider("Age", 20, 60, 30)
experience = st.slider("Years of Experience", 0, 40, 5)
salary = st.number_input("Salary", 20000, 200000, 50000)
training = st.slider("Training Hours", 0, 100, 20)
projects = st.slider("Projects Handled", 1, 20, 5)
satisfaction = st.slider("Work Environment Satisfaction (1-5)", 1, 5, 3)
rating = st.slider("Last Performance Rating (1-5)", 1, 5, 3)

# -----------------------------
# 5. Prepare Input
# -----------------------------
input_dict = {
    'Age': age,
    'Years_Experience': experience,
    'Salary': salary,
    'Training_Hours': training,
    'Projects_Handled': projects,
    'Work_Environment_Satisfaction': satisfaction,
    'Last_Performance_Rating': rating
}

# Add missing columns with 0
for col in X.columns:
    if col not in input_dict:
        input_dict[col] = 0

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Ensure column order matches training data
input_df = input_df[X.columns]

# -----------------------------
# 6. Prediction
# -----------------------------
if st.button("Predict Performance"):

    prediction = model.predict(input_df)[0]

    # Convert numeric → label
    if prediction == 0:
        result = "Low"
    elif prediction == 1:
        result = "Medium"
    else:
        result = "High"

    # Show result
    st.success(f"Predicted Performance: {result}")

    # -----------------------------
    # 7. Recommendation
    # -----------------------------
    st.write("### 💡 Recommendation")

    if prediction == 0:
        st.warning("Employee needs training and support")
    elif prediction == 1:
        st.info("Employee performing moderately, can improve")
    else:
        st.success("High performer – consider promotion")