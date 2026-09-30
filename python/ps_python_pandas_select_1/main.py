import pandas as pd
df = pd.read_csv("used_cars.csv")
selected_columns = df[["type", "mileage", "name"]]
print(selected_columns)
