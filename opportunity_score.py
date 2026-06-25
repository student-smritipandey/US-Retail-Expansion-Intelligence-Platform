import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load master dataset
df = pd.read_csv("master_county_only.csv")

print("Rows loaded:", len(df))

# Remove missing values (if any)
df = df.dropna(subset=[
    "Population_2023",
    "Education_Percent",
    "Unemployment_Rate",
    "Competitor_Density"
])

# -----------------------------
# Competitor Density per 100k Population
# -----------------------------
df["Competitor_Density_Ratio"] = (
    df["Competitor_Density"] /
    (df["Population_2023"] / 100000)
)

# -----------------------------
# Normalize Variables
# -----------------------------
scaler = MinMaxScaler()

df["Pop_Score"] = scaler.fit_transform(
    df[["Population_2023"]]
)

df["Edu_Score"] = scaler.fit_transform(
    df[["Education_Percent"]]
)

df["Unemp_Score"] = scaler.fit_transform(
    df[["Unemployment_Rate"]]
)

df["Comp_Score"] = scaler.fit_transform(
    df[["Competitor_Density_Ratio"]]
)

# -----------------------------
# Opportunity Score Formula
# -----------------------------
df["Opportunity_Score"] = (
      0.40 * df["Pop_Score"]
    + 0.30 * df["Edu_Score"]
    - 0.15 * df["Unemp_Score"]
    - 0.15 * df["Comp_Score"]
)

# -----------------------------
# Sort by Opportunity Score
# -----------------------------
df = df.sort_values(
    by="Opportunity_Score",
    ascending=False
)

# -----------------------------
# Top 20 Counties
# -----------------------------
top20 = df.head(20)

# -----------------------------
# Save Full Dataset
# -----------------------------
df.to_csv(
    "retail_opportunity_final.csv",
    index=False
)

# -----------------------------
# Save Top 20 Dataset
# -----------------------------
top20.to_csv(
    "top20_opportunities.csv",
    index=False
)

# -----------------------------
# Display Results
# -----------------------------
print("\nTop 20 Counties:")
print(
    top20[
        [
            "County",
            "State",
            "Opportunity_Score"
        ]
    ]
)

print("\nTop County Details:")
print(top20.iloc[0])

print("\nFiles Created Successfully:")
print("1. retail_opportunity_final.csv")
print("2. top20_opportunities.csv")

print("\nTotal Counties Analyzed:", len(df))