# ============================================
# CHUNK 12: CREATE SUMMARY REPORT
# ============================================

import os
import pandas as pd

print("Step 12: Creating summary report...")

# Get the directory of this Python file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to the input CSV
csv_path = os.path.join(
    script_dir,
    "..",
    "data",
    "Cyber Threat Intelligence_final_kaggle_cyber_dataset.csv"
)

# Create the visualizations folder if it doesn't exist
visualization_dir = os.path.join(script_dir, "..", "visualizations")
os.makedirs(visualization_dir, exist_ok=True)

# Output file path
summary_file = os.path.join(
    visualization_dir,
    "exploration_summary.txt"
)

# Load the dataset
df = pd.read_csv(csv_path)

# Create the summary report
with open(summary_file, "w", encoding="utf-8") as f:

    f.write("=" * 60 + "\n")
    f.write("DATA EXPLORATION SUMMARY\n")
    f.write("=" * 60 + "\n\n")

    f.write(f"Total records : {df.shape[0]:,}\n")
    f.write(f"Total features: {df.shape[1]}\n\n")

    f.write("Column Names\n")
    f.write("-" * 60 + "\n")

    for col in df.columns:
        f.write(f"- {col}\n")

    # Top Countries
    if "country_name" in df.columns:
        f.write("\nTop 10 Countries\n")
        f.write("-" * 60 + "\n")
        for country, count in df["country_name"].value_counts().head(10).items():
            f.write(f"{country}: {count:,}\n")

    # Continents
    if "continent" in df.columns:
        f.write("\nContinent Distribution\n")
        f.write("-" * 60 + "\n")
        for continent, count in df["continent"].value_counts().items():
            f.write(f"{continent}: {count:,}\n")

    # Weekdays
    if "reported_weekday" in df.columns:
        f.write("\nWeekday Distribution\n")
        f.write("-" * 60 + "\n")
        for day, count in df["reported_weekday"].value_counts().items():
            f.write(f"{day}: {count:,}\n")

print(f"\n✅ Summary report saved successfully!\n{summary_file}")

# Display a quick summary
print("\n" + "=" * 60)
print("QUICK SUMMARY")
print("=" * 60)

print(f"Records : {df.shape[0]:,}")
print(f"Features: {df.shape[1]}")

if "country_name" in df.columns:
    print(f"Countries : {df['country_name'].nunique()}")

if "continent" in df.columns:
    print(f"Continents: {df['continent'].nunique()}")

if "reported_weekday" in df.columns:
    print(f"Weekdays  : {df['reported_weekday'].nunique()}")

print("=" * 60)
print("✅ Data exploration completed successfully.")
print("=" * 60)