# ============================================
# CHUNK 7: CREATE COUNTRY CHART
# ============================================

import os
import pandas as pd
import matplotlib.pyplot as plt

print("Step 7: Creating country distribution chart...")

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
if 'country_name' not in df.columns:
    print("❌ Column 'country_name' not found in the dataset.")
else:
    # Get top 10 countries
    top_countries = df['country_name'].value_counts().head(10)

    print("\nTop 10 countries:")
    for country, count in top_countries.items():
        print(f"   {country}: {count}")

    # Create the chart
    plt.figure(figsize=(12, 6))
    plt.bar(top_countries.index, top_countries.values)
    plt.title('Top 10 Countries with Suspicious IPs', fontsize=16)
    plt.xlabel('Country')
    plt.ylabel('Number of IPs')
    plt.xticks(rotation=45, ha='right')

    # Save the chart
    output_path = os.path.join(visualization_dir, "country_chart.png")
    plt.tight_layout()
    plt.savefig(output_path)

    print(f"\n✅ Chart saved as:\n{output_path}")

    # Show the chart
    plt.show()