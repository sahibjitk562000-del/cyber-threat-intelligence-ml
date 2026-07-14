# ============================================
# CHUNK 6: COUNT VALUES IN KEY COLUMNS
# ============================================

import os
import pandas as pd

print("Step 6: Counting values in key columns...")

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

# Label distribution
if 'label' in df.columns:
    print("\n Label distribution:")
    print(df['label'].value_counts())
else:
    print("\n Column 'label' not found.")

# Country distribution (Top 10)
if 'country_name' in df.columns:
    print("\n Top 10 Countries:")
    print(df['country_name'].value_counts().head(10))
else:
    print("\n Column 'country_name' not found.")

# Continent distribution
if 'continent' in df.columns:
    print("\n Continent distribution:")
    print(df['continent'].value_counts())
else:
    print("\n Column 'continent' not found.")

# Weekday distribution
if 'reported_weekday' in df.columns:
    print("\n Weekday distribution:")
    print(df['reported_weekday'].value_counts())
else:
    print("\n Column 'reported_weekday' not found.")