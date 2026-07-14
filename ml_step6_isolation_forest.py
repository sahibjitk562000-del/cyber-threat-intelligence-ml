# ============================================
# CHUNK 6: BUILD ISOLATION FOREST
# ============================================

import os
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

print("=" * 60)
print("CHUNK 6: ISOLATION FOREST")
print("=" * 60)

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
splits_file = os.path.join(
    script_dir,
    "..",
    "data",
    "splits.pkl"
)

encoded_file = os.path.join(
    script_dir,
    "..",
    "data",
    "cyber_threat_intelligence_encoded.csv"
)

results_file = os.path.join(
    script_dir,
    "..",
    "data",
    "iso_results.pkl"
)

# Check required files
if not os.path.exists(splits_file):
    raise FileNotFoundError(
        f"File not found:\n{splits_file}\n\n"
        "Please run CHUNK 3 first."
    )

if not os.path.exists(encoded_file):
    raise FileNotFoundError(
        f"File not found:\n{encoded_file}\n\n"
        "Please run CHUNK 2 first."
    )

# Load train-test split (used only for consistency)
with open(splits_file, "rb") as f:
    data = pickle.load(f)

# Load the full encoded dataset
df = pd.read_csv(encoded_file)

# Separate features and target
X_full = df.drop("label", axis=1)
y_full = df["label"]

print(f"Full dataset: {X_full.shape[0]} samples")

# Create and train Isolation Forest
print("\nTraining Isolation Forest...")

iso_model = IsolationForest(
    contamination=0.10,
    n_estimators=100,
    random_state=42
)

iso_model.fit(X_full)

print("✅ Isolation Forest trained!")

# Predict anomalies
# Isolation Forest returns:
#  1  = Normal
# -1  = Anomaly

iso_pred = iso_model.predict(X_full)

# Convert predictions to binary labels
# 1 = Malicious (Anomaly)
# 0 = Benign (Normal)

iso_binary = (iso_pred == -1).astype(int)

# Calculate evaluation metrics
accuracy = accuracy_score(y_full, iso_binary)
precision = precision_score(
    y_full,
    iso_binary,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_full,
    iso_binary,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_full,
    iso_binary,
    average="weighted",
    zero_division=0
)

print("\n📊 Isolation Forest Performance:")
print("-" * 40)
print(f"   Accuracy:  {accuracy:.4f}")
print(f"   Precision: {precision:.4f}")
print(f"   Recall:    {recall:.4f}")
print(f"   F1-Score:  {f1:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_full, iso_binary)

print("\nConfusion Matrix:")
print(cm)

# Anomaly statistics
anomaly_count = np.sum(iso_binary)
normal_count = len(iso_binary) - anomaly_count

print("\n📊 Anomaly Detection Results:")
print(f"   Anomalies detected: {anomaly_count} ({anomaly_count / len(iso_binary) * 100:.1f}%)")
print(f"   Normal points:      {normal_count} ({normal_count / len(iso_binary) * 100:.1f}%)")

# Save results
results = {
    "model": iso_model,
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1": f1,
    "confusion_matrix": cm,
    "y_pred": iso_binary,
    "anomaly_count": anomaly_count,
    "normal_count": normal_count
}

with open(results_file, "wb") as f:
    pickle.dump(results, f)

print("\n✅ Isolation Forest results saved successfully!")
print(f"Location: {results_file}")