# ============================================
# CHUNK 3: SPLIT INTO FEATURES AND TARGET
# ============================================

import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("=" * 60)
print("CHUNK 3: FEATURE-TARGET SPLIT")
print("=" * 60)

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output paths
input_csv = os.path.join(
    script_dir,
    "..",
    "data",
    "cyber_threat_intelligence_encoded.csv"
)

output_pickle = os.path.join(
    script_dir,
    "..",
    "data",
    "splits.pkl"
)

# Check if encoded dataset exists
if not os.path.exists(input_csv):
    raise FileNotFoundError(
        f"Encoded dataset not found:\n{input_csv}\n\n"
        "Please run Chunk 2 first."
    )

# Load encoded dataset
df = pd.read_csv(input_csv)

print(f"\nData shape: {df.shape}")

# Check target column
if "label" not in df.columns:
    raise ValueError("Column 'label' not found in the dataset.")

# Separate features and target
X = df.drop("label", axis=1)
y = df["label"]

print(f"\nFeatures (X): {X.shape}")
print(f"Target (y): {y.shape}")

# Target distribution
print("\nTarget distribution:")
print(y.value_counts())

# Scale features
print("\nScaling features...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"Features scaled successfully!")
print(f"Scaled feature shape: {X_scaled.shape}")

# Split data
print("\nSplitting into training and testing sets...")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples : {X_test.shape[0]}")

# Save everything for later use
with open(output_pickle, "wb") as f:
    pickle.dump({
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "feature_names": X.columns.tolist(),
        "scaler": scaler
    }, f)

print(f"\n Data splits saved successfully!")
print(output_pickle)