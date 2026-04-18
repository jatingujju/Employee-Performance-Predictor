import pandas as pd
import numpy as np
import random
import os

# -----------------------------
# 1. Create Data folder
# -----------------------------
if not os.path.exists("Data"):
    os.makedirs("Data")

# -----------------------------
# 2. Parameters
# -----------------------------
n = 1000

departments = ['Sales', 'IT', 'HR', 'Finance', 'Marketing']
education_levels = ['Bachelors', 'Masters', 'PhD']
job_roles = ['Manager', 'Executive', 'Analyst', 'Engineer', 'Consultant']

data = []

# -----------------------------
# 3. Data Generation
# -----------------------------
for i in range(n):
    employee_id = i + 1
    age = np.random.randint(21, 60)
    gender = random.choice(['Male', 'Female'])
    department = random.choice(departments)
    education = random.choice(education_levels)
    experience = np.random.randint(0, age - 20)

    salary = np.random.randint(20000, 150000)
    training_hours = np.random.randint(0, 100)
    job_role = random.choice(job_roles)

    work_env = np.random.randint(1, 6)
    last_rating = np.random.randint(1, 6)
    projects = np.random.randint(1, 15)
    overtime = random.choice(['Yes', 'No'])

    # -----------------------------
    # 4. Performance Logic (FINAL BALANCED)
    # -----------------------------
    score = (
        experience * 0.3 +
        training_hours * 0.2 +
        work_env * 5 +
        last_rating * 10 +
        projects * 1.5
    )

    if score > 85:
        performance = 'High'
    elif score > 50:
        performance = 'Medium'
    else:
        performance = 'Low'

    data.append([
        employee_id, age, gender, department, education,
        experience, salary, training_hours, job_role,
        work_env, last_rating, projects, overtime, performance
    ])

# -----------------------------
# 5. Create DataFrame
# -----------------------------
columns = [
    'Employee_ID', 'Age', 'Gender', 'Department', 'Education_Level',
    'Years_Experience', 'Salary', 'Training_Hours', 'Job_Role',
    'Work_Environment_Satisfaction', 'Last_Performance_Rating',
    'Projects_Handled', 'Overtime', 'Performance'
]

df = pd.DataFrame(data, columns=columns)

# -----------------------------
# 6. Save Dataset
# -----------------------------
file_path = os.path.join("Data", "employee_performance_data.csv")
df.to_csv(file_path, index=False)

# -----------------------------
# 7. Output
# -----------------------------
print("✅ Dataset generated successfully!")
print("Saved at:", file_path)

print("\nSample Data:\n")
print(df.head())

print("\n📊 Performance Distribution:\n")
print(df['Performance'].value_counts())