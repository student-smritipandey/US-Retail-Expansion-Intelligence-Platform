import pandas as pd

# Load data
df = pd.read_csv("Education2023.csv", encoding="latin1")

# Keep only Bachelor's % (latest period)
df = df[
    df["Attribute"] ==
    "Percent of adults with a bachelor's degree or higher, 2019-23"
]

# Remove national-level rows
df = df[df["State"] != "US"]

# Keep required columns
df = df[["FIPS Code", "State", "Area name", "Value"]]

# Rename columns
df.columns = ["FIPS", "State", "County", "Education_Percent"]

# Save
df.to_csv("education_final.csv", index=False)

print(df.head())
print("Rows:", len(df))