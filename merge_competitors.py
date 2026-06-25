import pandas as pd

# Load files
master = pd.read_csv("master_county_data.csv")
starbucks = pd.read_csv("starbucks_state_counts.csv")
walmart = pd.read_csv("walmart_state_counts.csv")

# Merge Starbucks data using State column
master = pd.merge(
    master,
    starbucks,
    on="State",
    how="left"
)

# Merge Walmart data using State column
master = pd.merge(
    master,
    walmart,
    on="State",
    how="left"
)

# Fill missing values
master["Starbucks_Count"] = master["Starbucks_Count"].fillna(0)
master["Walmart_Count"] = master["Walmart_Count"].fillna(0)

# Create competitor density
master["Competitor_Density"] = (
    master["Starbucks_Count"] +
    master["Walmart_Count"]
)

# Save
master.to_csv("master_with_competitors.csv", index=False)

print(master.head())
print("Rows:", len(master))
print(master.columns)