# ============================================
# CHUNK 7: COMPARE ALL MODELS
# ============================================

import os
import pickle
import pandas as pd

print("=" * 60)
print("CHUNK 7: MODEL COMPARISON")
print("=" * 60)

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
dt_file = os.path.join(
    script_dir,
    "..",
    "data",
    "dt_results.pkl"
)

rf_file = os.path.join(
    script_dir,
    "..",
    "data",
    "rf_results.pkl"
)

iso_file = os.path.join(
    script_dir,
    "..",
    "data",
    "iso_results.pkl"
)

visualization_dir = os.path.join(
    script_dir,
    "..",
    "visualizations"
)

# Create visualizations folder if it doesn't exist
os.makedirs(visualization_dir, exist_ok=True)

comparison_file = os.path.join(
    visualization_dir,
    "model_comparison.csv"
)

all_results_file = os.path.join(
    visualization_dir,
    "all_model_results.csv"
)

# Check required files
required_files = [dt_file, rf_file, iso_file]

for file in required_files:
    if not os.path.exists(file):
        raise FileNotFoundError(
            f"\nRequired file not found:\n{file}\n"
            "Please run the previous model training chunks first."
        )

# Load Decision Tree results
with open(dt_file, "rb") as f:
    dt_results = pickle.load(f)

# Load Random Forest results
with open(rf_file, "rb") as f:
    rf_results = pickle.load(f)

# Load Isolation Forest results
with open(iso_file, "rb") as f:
    iso_results = pickle.load(f)

# Create comparison table
comparison = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "Random Forest",
        "Isolation Forest"
    ],
    "Accuracy": [
        dt_results["accuracy"],
        rf_results["accuracy"],
        iso_results["accuracy"]
    ],
    "Precision": [
        dt_results["precision"],
        rf_results["precision"],
        iso_results["precision"]
    ],
    "Recall": [
        dt_results["recall"],
        rf_results["recall"],
        iso_results["recall"]
    ],
    "F1-Score": [
        dt_results["f1"],
        rf_results["f1"],
        iso_results["f1"]
    ]
})

print("\n Model Performance Comparison")
print("-" * 70)
print(comparison.to_string(index=False))
print("-" * 70)

# Find best model
best_idx = comparison["Accuracy"].idxmax()
best_model = comparison.iloc[best_idx]["Model"]
best_accuracy = comparison.iloc[best_idx]["Accuracy"]

print(f"\n Best Performing Model: {best_model}")
print(f"Accuracy: {best_accuracy:.4f}")

# Save comparison table
comparison.to_csv(comparison_file, index=False)

print("\n Model comparison saved successfully!")
print(comparison_file)

# Save all results
all_results = pd.DataFrame([
    {
        "Model": "Decision Tree",
        "Accuracy": dt_results["accuracy"],
        "Precision": dt_results["precision"],
        "Recall": dt_results["recall"],
        "F1-Score": dt_results["f1"]
    },
    {
        "Model": "Random Forest",
        "Accuracy": rf_results["accuracy"],
        "Precision": rf_results["precision"],
        "Recall": rf_results["recall"],
        "F1-Score": rf_results["f1"]
    },
    {
        "Model": "Isolation Forest",
        "Accuracy": iso_results["accuracy"],
        "Precision": iso_results["precision"],
        "Recall": iso_results["recall"],
        "F1-Score": iso_results["f1"]
    }
])

all_results.to_csv(all_results_file, index=False)

print("All model results saved successfully!")
print(all_results_file)