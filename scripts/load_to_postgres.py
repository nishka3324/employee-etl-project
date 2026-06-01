import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("../data/employees.csv")

df["salary"] = df["salary"].fillna(df["salary"].mean())
df["name"] = df["name"].fillna("Unknown")

engine = create_engine(
    "postgresql://postgres:nishkaks@localhost:5434/employee_db"

)

df.to_sql(
    "employees",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")