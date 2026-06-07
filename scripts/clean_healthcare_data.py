import pandas as pd

# Read dataset
df = pd.read_csv("data/healthcare_dataset.csv")

# Remove duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = (
    df.columns
      .str.lower()
      .str.replace(" ", "_")
)

# Convert dates
df["date_of_admission"] = pd.to_datetime(df["date_of_admission"])
df["discharge_date"] = pd.to_datetime(df["discharge_date"])

# Create length of stay column
df["length_of_stay"] = (
    df["discharge_date"] - df["date_of_admission"]
).dt.days

# Save cleaned file
df.to_csv("output/healthcare_cleaned.csv", index=False)

print("Cleaning completed!")
print("Final shape:", df.shape)