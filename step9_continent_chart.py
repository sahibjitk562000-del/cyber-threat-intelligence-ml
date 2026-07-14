# ============================================
# CHUNK 9: CREATE CONTINENT CHART (PIE CHART)
# ============================================

import os
import pandas as pd
import matplotlib.pyplot as plt

print("Step 9: Creating continent distribution chart...")

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
if 'continent' not in df.columns:
    print("❌ Column 'continent' not found in the dataset.")
else:
    # Get continent counts
    continent_counts = df['continent'].value_counts()

    print("\nContinent distribution:")
    for continent, count in continent_counts.items():
        print(f"   {continent}: {count}")

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        continent_counts.values,
        labels=continent_counts.index,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title('Distribution of Suspicious IPs by Continent', fontsize=16)
    plt.axis('equal')  # Keep the pie chart circular

    # Save the chart
    output_path = os.path.join(visualization_dir, "continent_chart.png")
    plt.tight_layout()
    plt.savefig(output_path)

    print(f"\n✅ Chart saved as:\n{output_path}")

    # Show the chart
    plt.show()