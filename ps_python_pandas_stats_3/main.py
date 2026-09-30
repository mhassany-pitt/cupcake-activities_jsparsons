import pandas as pd
df = pd.read_csv("used_cars.csv")
print("Value counts for type:", df["type"].value_counts().head())
