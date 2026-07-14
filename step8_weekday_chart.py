# ============================================
# CHUNK 8: CREATE WEEKDAY CHART
# ============================================

import os
import pandas as pd
import matplotlib.pyplot as plt

print("Step 8: Creating weekday distribution chart...")

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
if 'reported_weekday' not in df.columns:
    print("❌ Column 'reported_weekday' not found in the dataset.")
else:
    # Get weekday counts
    weekday_counts = df['reported_weekday'].value_counts()

    # Order days correctly
    day_order = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]
    weekday_counts = weekday_counts.reindex(day_order, fill_value=0)

    print("\nWeekday distribution:")
    for day, count in weekday_counts.items():
        print(f"   {day}: {count}")

    # Create the chart
    plt.figure(figsize=(12, 6))
    plt.bar(weekday_counts.index, weekday_counts.values)
    plt.title('Threat Reports by Day of Week', fontsize=16)
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Reports')

    # Save the chart
    output_path = os.path.join(visualization_dir, "weekday_chart.png")
    plt.tight_layout()
    plt.savefig(output_path)

    print(f"\n✅ Chart saved as:\n{output_path}")

    # Show the chart
    plt.show()