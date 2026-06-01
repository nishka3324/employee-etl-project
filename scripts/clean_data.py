import pandas as pd

df = pd.read_csv("../data/employees.csv")

print("ORIGINAL DATA:")
print(df)

df["salary"] = df["salary"].fillna(df["salary"].mean())

df["name"] = df["name"].fillna("Unknown")

print("\nUPDATED DATA:")
print(df)

it_employees = df[df["department"] == "IT"]

print("\nIT EMPLOYEES:")
print(it_employees)

df["bonus"] = df["salary"] * 0.10

print("\nDATA WITH BONUS:")
print(df)

df.to_csv("../output/cleaned_employees.csv", index=False)

print("\nCleaned file saved successfully!")
