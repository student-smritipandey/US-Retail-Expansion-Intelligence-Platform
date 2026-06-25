import pandas as pd

pop = pd.read_csv("population_final.csv")
edu = pd.read_csv("education_final.csv")
unemp = pd.read_csv("unemployment_final.csv")

# Merge on FIPS
master = pop.merge(
    edu[["FIPS", "Education_Percent"]],
    on="FIPS",
    how="inner"
)

master = master.merge(
    unemp[["FIPS", "Unemployment_Rate"]],
    on="FIPS",
    how="inner"
)

master.to_csv("master_county_data.csv", index=False)

print(master.head())
print("Rows:", len(master))