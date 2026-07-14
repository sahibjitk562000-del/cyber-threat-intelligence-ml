# ============================================
# CHUNK 11: SAVE PROCESSED DATA
# ============================================

import os
import pandas as pd

print("Step 11: Saving processed data...")

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to the input CSV
input_csv = os.path.join(
    script_dir,
    "..",
    "data",
    "Cyber Threat Intelligence_final_kaggle_cyber_dataset.csv"
)

# Build the path to the output CSV
output_csv = os.path.join(
    script_dir,
    "..",
    "data",
    "cyber_threat_intelligence_processed.csv"
)

# Load the dataset
df = pd.read_csv(input_csv)

# Drop unnecessary columns (if they exist)
columns_to_drop = [
    'ip_address',
    'last_reported_at',
    'country_code',
    'reported_date'
]

df_processed = df.drop(columns=columns_to_drop, errors='ignore')

# Handle missing values
df_processed = df_processed.fillna('Unknown')

# Save processed dataset
df_processed.to_csv(output_csv, index=False)

print("\n✅ Processed data saved successfully!")
print(f"Original shape : {df.shape}")
print(f"Processed shape: {df_processed.shape}")
print(f"Saved to       : {output_csv}")