import pandas as pd

# Load Walmart data
df = pd.read_csv("walmart_2018_11_06.csv")

# Count stores by state
state_counts = (
    df.groupby("state")
      .size()
      .reset_index(name="Walmart_Count")
)

# Rename column
state_counts.columns = ["State", "Walmart_Count"]

# Convert state codes to uppercase
state_counts["State"] = state_counts["State"].str.upper()

# Save
state_counts.to_csv("walmart_state_counts.csv", index=False)

print(state_counts.head())
print("States:", len(state_counts))
print("Total Walmart Stores:", state_counts["Walmart_Count"].sum())