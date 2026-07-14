# ============================================
# CHUNK 8: CREATE FINAL CHARTS
# ============================================

import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("=" * 60)
print("CHUNK 8: CREATING FINAL CHARTS")
print("=" * 60)

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create visualizations folder
visualization_dir = os.path.join(script_dir, "..", "visualizations")
os.makedirs(visualization_dir, exist_ok=True)

# File paths
dt_file = os.path.join(script_dir, "..", "data", "dt_results.pkl")
rf_file = os.path.join(script_dir, "..", "data", "rf_results.pkl")
iso_file = os.path.join(script_dir, "..", "data", "iso_results.pkl")

# Check required files
required_files = [dt_file, rf_file, iso_file]

for file in required_files:
    if not os.path.exists(file):
        raise FileNotFoundError(
            f"\nRequired file not found:\n{file}\n"
            "Please run the previous model training chunks first."
        )

# Load results
with open(dt_file, "rb") as f:
    dt_results = pickle.load(f)

with open(rf_file, "rb") as f:
    rf_results = pickle.load(f)

with open(iso_file, "rb") as f:
    iso_results = pickle.load(f)

# ============================================
# CHART 1: CONFUSION MATRICES
# ============================================

print("\n1. Creating Confusion Matrices...")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Decision Tree
sns.heatmap(
    dt_results["confusion_matrix"],
    annot=True,
    fmt="d",
    cmap="Blues",
    ax=axes[0]
)
axes[0].set_title("Decision Tree")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Actual")

# Random Forest
sns.heatmap(
    rf_results["confusion_matrix"],
    annot=True,
    fmt="d",
    cmap="Greens",
    ax=axes[1]
)
axes[1].set_title("Random Forest")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")

# Isolation Forest
sns.heatmap(
    iso_results["confusion_matrix"],
    annot=True,
    fmt="d",
    cmap="Oranges",
    ax=axes[2]
)
axes[2].set_title("Isolation Forest")
axes[2].set_xlabel("Predicted")
axes[2].set_ylabel("Actual")

plt.tight_layout()

confusion_path = os.path.join(
    visualization_dir,
    "confusion_matrices.png"
)

plt.savefig(
    confusion_path,
    dpi=300,
    bbox_inches="tight"
)

print(f"   ✅ Saved:\n   {confusion_path}")

# ============================================
# CHART 2: FEATURE IMPORTANCE
# ============================================

print("\n2. Creating Feature Importance Chart...")

importances = rf_results["feature_importances"]
feature_names = rf_results["feature_names"]

imp_df = pd.DataFrame({
    "feature": feature_names,
    "importance": importances
}).sort_values(
    "importance",
    ascending=False
)

plt.figure(figsize=(12, 8))

bars = plt.barh(
    imp_df.head(10)["feature"],
    imp_df.head(10)["importance"]
)

plt.xlabel("Feature Importance", fontsize=14)
plt.title(
    "Top 10 Features for Threat Detection (Random Forest)",
    fontsize=16
)

plt.gca().invert_yaxis()

# Add labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.005,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.3f}",
        va="center",
        fontsize=10
    )

plt.tight_layout()

feature_path = os.path.join(
    visualization_dir,
    "feature_importance.png"
)

plt.savefig(
    feature_path,
    dpi=300,
    bbox_inches="tight"
)

print(f"   ✅ Saved:\n   {feature_path}")

# ============================================
# CHART 3: MODEL COMPARISON
# ============================================

print("\n3. Creating Model Comparison Chart...")

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1-Score"
]

x = np.arange(len(metrics))
width = 0.25

dt_values = [
    dt_results["accuracy"],
    dt_results["precision"],
    dt_results["recall"],
    dt_results["f1"]
]

rf_values = [
    rf_results["accuracy"],
    rf_results["precision"],
    rf_results["recall"],
    rf_results["f1"]
]

iso_values = [
    iso_results["accuracy"],
    iso_results["precision"],
    iso_results["recall"],
    iso_results["f1"]
]

fig, ax = plt.subplots(figsize=(12, 6))

bars1 = ax.bar(
    x - width,
    dt_values,
    width,
    label="Decision Tree"
)

bars2 = ax.bar(
    x,
    rf_values,
    width,
    label="Random Forest"
)

bars3 = ax.bar(
    x + width,
    iso_values,
    width,
    label="Isolation Forest"
)

# Add labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.01,
            f"{height:.3f}",
            ha="center",
            fontsize=9
        )

ax.set_xlabel("Metrics", fontsize=14)
ax.set_ylabel("Score", fontsize=14)
ax.set_title("Model Performance Comparison", fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()
ax.set_ylim(0, 1.1)

plt.tight_layout()

comparison_path = os.path.join(
    visualization_dir,
    "model_comparison.png"
)

plt.savefig(
    comparison_path,
    dpi=300,
    bbox_inches="tight"
)

print(f" Saved:\n   {comparison_path}")

plt.show()

print("\n" + "=" * 60)
print(" ALL CHARTS CREATED SUCCESSFULLY!")
print("=" * 60)

print("\n Files saved:")

print(f"• {confusion_path}")
print(f"• {feature_path}")
print(f"• {comparison_path}")