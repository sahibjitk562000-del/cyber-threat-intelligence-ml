# ============================================
# CHUNK 2: ENCODE CATEGORICAL VARIABLES
# ============================================

import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("CHUNK 2: ENCODE CATEGORICAL VARIABLES")
print("=" * 60)

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output file paths
input_csv = os.path.join(
    script_dir,
    "..",
    "data",
    "cyber_threat_intelligence_processed.csv"
)

output_csv = os.path.join(
    script_dir,
    "..",
    "data",
    "cyber_threat_intelligence_encoded.csv"
)

# Check that the processed dataset exists
if not os.path.exists(input_csv):
    raise FileNotFoundError(
        f"Processed dataset not found:\n{input_csv}\n\n"
        "Please run Section 3 - Chunk 11 first."
    )

# Load the processed dataset
df = pd.read_csv(input_csv)

print(f"\nOriginal data shape: {df.shape}")

# Find categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

print("\nCategorical columns found:")
for col in categorical_cols:
    print(f" - {col}")

# Encode categorical columns
print("\nEncoding categorical columns...")

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le
    print(f"   ✅ {col}")

print("\nEncoding completed successfully!")

print("\nData types after encoding:")
print(df.dtypes.value_counts())

# Save the encoded dataset
df.to_csv(output_csv, index=False)

print(f"\n Encoded dataset saved successfully!")
print(output_csv)

print("\nFirst 3 rows:")
print(df.head(3))