import pandas as pd

# Load file
df = pd.read_csv("PopulationEstimates.csv", encoding="latin1")
# Keep only population estimates for 2023
df = df[df["Attribute"] == "POP_ESTIMATE_2023"]

# Remove national-level rows
df = df[df["State"] != "US"]

# Keep required columns
df = df[["FIPStxt", "State", "Area_Name", "Value"]]

# Rename columns
df.columns = ["FIPS", "State", "County", "Population_2023"]

# Save
df.to_csv("population_final.csv", index=False)

print(df.head())
print("Rows:", len(df))