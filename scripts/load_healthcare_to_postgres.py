import pandas as pd
from sqlalchemy import create_engine

# Read cleaned data
df = pd.read_csv("output/healthcare_cleaned.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:nishkaks@localhost:5434/postgres"
)

# Load data
df.to_sql(
    "healthcare_records",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")
print("Rows loaded:", len(df))