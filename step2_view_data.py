# ============================================
# CHUNK 2: VIEW FIRST 5 ROWS
# ============================================

import os
import pandas as pd

print("Step 2: Viewing first 5 rows...")

# Get the directory where this Python file is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the CSV file
csv_path = os.path.join(
    script_dir,
    "..",
    "data",
    "Cyber Threat Intelligence_final_kaggle_cyber_dataset.csv"
)

# Load the dataset
df = pd.read_csv(csv_path)

# Show first 5 rows
print("\nFirst 5 rows of data:")
print(df.head())