●
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv("employee_features.csv")  # one row per employee per cycle
assert df['employee_id'].is_unique

# basic tests
rules = {
  'experience_years': (0, 45),
  'on_time_delivery_rate': (0, 1),
  'manager_score': (0, 5),
  'peer_feedback_score': (0, 5),
  'avg_task_delay_days': (-10, 60),
}
for col,(lo,hi) in rules.items():
    bad = df[(df[col]<lo) | (df[col]>hi)]
    print(col, "out_of_range:", len(bad))

# stratified split on target
train, test = train_test_split(df, test_size=0.2, random_state=13,
stratify=df['perf_band_next'])
