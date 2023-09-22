import pandas as pd
df = pd.read_csv("data.csv")
x=df["Date"].median()
df["Date"].fillna(x, inplace=True)
print(df)