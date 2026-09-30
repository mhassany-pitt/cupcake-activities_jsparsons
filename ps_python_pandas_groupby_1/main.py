import pandas as pd
df = pd.read_csv("used_cars.csv")
grouped_by_type = df.groupby("type")["mileage"].mean()
print(grouped_by_type)
