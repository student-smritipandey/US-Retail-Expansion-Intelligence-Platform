import pandas as pd

# Load Starbucks data
df = pd.read_csv("starbucks location.csv")

# Keep only US stores
us = df[df["Country"] == "US"]

# Count stores by state
state_counts = (
    us.groupby("State/Province")
      .size()
      .reset_index(name="Starbucks_Count")
)

# Rename column
state_counts.columns = ["State", "Starbucks_Count"]

# Save
state_counts.to_csv("starbucks_state_counts.csv", index=False)

print(state_counts.head())
print("States:", len(state_counts))
print("US Stores:", state_counts["Starbucks_Count"].sum())