import pandas as pd
df = pd.read_csv("used_cars.csv")
grouped_by_type = df.groupby("type")["mileage"].max()
print(grouped_by_type)
