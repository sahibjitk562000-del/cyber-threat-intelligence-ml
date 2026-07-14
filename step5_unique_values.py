# ============================================
# CHUNK 5: CHECK UNIQUE VALUES
# ============================================

import os
import pandas as pd

print("Step 5: Checking unique values...")

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to the CSV file
csv_path = os.path.join(
    script_dir,
    "..",
    "data",
    "Cyber Threat Intelligence_final_kaggle_cyber_dataset.csv"
)

# Load the dataset
df = pd.read_csv(csv_path)

# Key columns to check
key_columns = [
    'label',
    'abuse_confidence_score',
    'severity',
    'risk_level',
    'reported_weekday',
    'time_zone_attack',
    'continent'
]

print("\nUnique values in key columns:")
print("-" * 40)

for col in key_columns:
    if col in df.columns:
        unique_vals = sorted(df[col].dropna().unique(), key=str)

        print(f"\n{col}:")
        print(f"   Number of unique values: {len(unique_vals)}")
        print(f"   Values: {unique_vals}")
    else:
        print(f"\n Column '{col}' not found in the dataset.")