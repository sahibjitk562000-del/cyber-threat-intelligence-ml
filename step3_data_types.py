# ============================================
# CHUNK 3: CHECK DATA TYPES
# ============================================


import os
import pandas as pd

print("Step 3: Checking data types...")

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    script_dir,
    "..",
    "data",
    "Cyber Threat Intelligence_final_kaggle_cyber_dataset.csv"
)

df = pd.read_csv(csv_path)

print("\nData types of each column:")
print(df.dtypes)