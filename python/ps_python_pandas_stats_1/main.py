import pandas as pd
df = pd.read_csv("used_cars.csv")
print("First 5 rows:", df.head(5))
average_mileage = df["mileage"].mean()
print("Average mileage:", average_mileage)
