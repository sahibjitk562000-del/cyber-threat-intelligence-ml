# ============================================
# CHUNK 10: CREATE HOUR DISTRIBUTION CHART
# ============================================

import os
import pandas as pd
import matplotlib.pyplot as plt

print("Step 10: Creating hour distribution chart...")

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to the CSV file
csv_path = os.path.join(
    script_dir,
    "..",
    "data",
    "Cyber Threat Intelligence_final_kaggle_cyber_dataset.csv"
)

# Create the visualizations folder if it doesn't exist
visualization_dir = os.path.join(script_dir, "..", "visualizations")
os.makedirs(visualization_dir, exist_ok=True)

# Load the dataset
df = pd.read_csv(csv_path)

# Check if the required column exists
if 'reported_hour' not in df.columns:
    print("❌ Column 'reported_hour' not found in the dataset.")
else:
    # Get hour counts
    hour_counts = df['reported_hour'].value_counts().sort_index()

    print("\nTop 5 busiest hours:")
    for hour, count in hour_counts.nlargest(5).items():
        print(f"   {int(hour):02d}:00 - {count}")

    # Create the chart
    plt.figure(figsize=(14, 6))
    plt.bar(hour_counts.index, hour_counts.values)
    plt.title("Threat Reports by Hour of Day", fontsize=16)
    plt.xlabel("Hour of Day (24-hour format)")
    plt.ylabel("Number of Reports")
    plt.xticks(range(0, 24))

    # Save the chart
    output_path = os.path.join(visualization_dir, "hour_chart.png")
    plt.tight_layout()
    plt.savefig(output_path)

    print(f"\n✅ Chart saved as:\n{output_path}")

    # Show the chart
    plt.show()