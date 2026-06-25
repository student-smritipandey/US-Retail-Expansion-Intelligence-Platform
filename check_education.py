import pandas as pd

df = pd.read_csv("Education2023.csv", encoding="latin1")

print(df["Attribute"].unique())