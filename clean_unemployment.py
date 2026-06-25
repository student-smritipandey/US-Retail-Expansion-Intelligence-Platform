import pandas as pd

# Load data
df = pd.read_csv("Unemployment2023.csv", encoding="latin1")

# Keep only unemployment rate
df = df[df["Attribute"] == "Unemployment_rate_2023"]

# Remove national-level rows
df = df[df["State"] != "US"]

# Keep required columns
df = df[["FIPS_Code", "State", "Area_Name", "Value"]]

# Rename columns
df.columns = ["FIPS", "State", "County", "Unemployment_Rate"]

# Save
df.to_csv("unemployment_final.csv", index=False)

print(df.head())
print("Rows:", len(df))