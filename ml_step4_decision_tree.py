# ============================================
# CHUNK 4: BUILD DECISION TREE
# ============================================

import os
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

print("=" * 60)
print("CHUNK 4: DECISION TREE")
print("=" * 60)

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths
splits_file = os.path.join(script_dir, "..", "data", "splits.pkl")
results_file = os.path.join(script_dir, "..", "data", "dt_results.pkl")

# Check if splits file exists
if not os.path.exists(splits_file):
    raise FileNotFoundError(
        f"'{splits_file}' not found.\n"
        "Please run Chunk 3 first."
    )

# Load the train-test splits
with open(splits_file, "rb") as f:
    data = pickle.load(f)

X_train = data["X_train"]
X_test = data["X_test"]
y_train = data["y_train"]
y_test = data["y_test"]

print(f"\nTraining samples : {X_train.shape[0]}")
print(f"Testing samples  : {X_test.shape[0]}")

# Build Decision Tree model
print("\nTraining Decision Tree model...")

dt_model = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)

dt_model.fit(X_train, y_train)

print("✅ Decision Tree trained successfully!")

# Predictions
y_pred = dt_model.predict(X_test)

# Evaluation metrics
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

print("\nModel Performance")
print("-" * 40)
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

# Save results
results = {
    "model": dt_model,
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1": f1,
    "confusion_matrix": cm,
    "y_pred": y_pred
}

with open(results_file, "wb") as f:
    pickle.dump(results, f)

print(f"\n Results saved successfully!")
print(results_file)