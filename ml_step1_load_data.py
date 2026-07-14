# ============================================
# SECTION 4: IMPLEMENTATION
# CHUNK 1: LOAD PROCESSED DATA
# ============================================

import os
import pandas as pd

print("=" * 60)
print("SECTION 4: IMPLEMENTATION")
print("CHUNK 1: LOAD PROCESSED DATA")
print("=" * 60)

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the processed dataset created in Section 3 (Chunk 11)
processed_csv = os.path.join(
    script_dir,
    "..",
    "data",
    "cyber_threat_intelligence_processed.csv"
)

# Check that the file exists
if not os.path.exists(processed_csv):
    raise FileNotFoundError(
        f"Processed dataset not found:\n{processed_csv}\n\n"
        "Please run Section 3 - Chunk 11 first."
    )

# Load the processed dataset
df = pd.read_csv(processed_csv)

print("\n Processed data loaded successfully!")
print(f"Shape   : {df.shape}")
print(f"Columns : {list(df.columns)}")

print("\nFirst 3 rows:")
print(df.head(3))