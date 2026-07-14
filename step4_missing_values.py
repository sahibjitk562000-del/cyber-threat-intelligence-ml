
# ============================================
# CHUNK 4: CHECK FOR MISSING VALUES
# ============================================

import os
import pandas as pd

print("Step 4: Checking for missing values...")

# Get the directory of this script
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

# Check missing values
missing = df.isnull().sum()
total_missing = missing.sum()

print(f"\nTotal missing values: {total_missing}")

if total_missing == 0:
    print("✅ No missing values found!")
else:
    print("\nColumns with missing values:")
    for col, count in missing.items():
        if count > 0:
            print(f"   • {col}: {count}")