import pandas as pd
df = pd.read_csv("used_cars.csv")
selected_columns = df[["type", "mileage", "name"]]
suv_cars = selected_columns[selected_columns["type"] == "SUV"]
print(suv_cars)
