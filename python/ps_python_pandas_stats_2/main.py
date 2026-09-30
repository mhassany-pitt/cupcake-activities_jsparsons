import pandas as pd
df = pd.read_csv("used_cars.csv")
print("Describe (type and mileage):", df[["type", "mileage"]].describe())
