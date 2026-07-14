# ============================================
# CHUNK 5: BUILD RANDOM FOREST
# ============================================

import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

print("=" * 60)
print("CHUNK 5: RANDOM FOREST")
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

results_file = os.path.join(
    script_dir,
    "..",
    "data",
    "rf_results.pkl"
)

# Check if splits file exists
if not os.path.exists(splits_file):
    raise FileNotFoundError(
        f"File not found:\n{splits_file}\n\n"
        "Please run CHUNK 3 first."
    )

# Load the train-test splits
with open(splits_file, "rb") as f:
    data = pickle.load(f)

X_train = data["X_train"]
X_test = data["X_test"]
y_train = data["y_train"]
y_test = data["y_test"]
feature_names = data["feature_names"]

print(f"Training set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# Create and train Random Forest
print("\nTraining Random Forest...")

rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)

rf_model.fit(X_train, y_train)

print("✅ Random Forest trained!")

# Make predictions
y_pred = rf_model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)
recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)
f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

print("\n📊 Random Forest Performance:")
print("-" * 40)
print(f"   Accuracy:  {accuracy:.4f}")
print(f"   Precision: {precision:.4f}")
print(f"   Recall:    {recall:.4f}")
print(f"   F1-Score:  {f1:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Feature Importance
importances = rf_model.feature_importances_

print("\n🔝 Top 5 Most Important Features:")

top_indices = np.argsort(importances)[-5:][::-1]

for i, idx in enumerate(top_indices, 1):
    print(f"   {i}. {feature_names[idx]}: {importances[idx]:.4f}")

# Save results
results = {
    "model": rf_model,
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1": f1,
    "confusion_matrix": cm,
    "y_pred": y_pred,
    "feature_importances": importances,
    "feature_names": feature_names
}

with open(results_file, "wb") as f:
    pickle.dump(results, f)

print("\n Random Forest results saved successfully!")
print(f"Location: {results_file}")