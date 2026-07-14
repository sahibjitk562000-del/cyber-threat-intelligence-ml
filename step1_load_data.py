# ============================================
# CHUNK 1: LOAD THE DATASET
# ============================================

import pandas as pd
import os

print("Step 1: Loading the dataset...")

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    script_dir,
    "..",
    "data",
    "Cyber Threat Intelligence_final_kaggle_cyber_dataset.csv"
)

print("CSV Path:", csv_path)

df = pd.read_csv(csv_path)

print(f"✅ Dataset loaded!")
print(f"   Rows: {df.shape[0]}")
print(f"   Columns: {df.shape[1]}")
print(f"   Column names: {df.columns.tolist()}")