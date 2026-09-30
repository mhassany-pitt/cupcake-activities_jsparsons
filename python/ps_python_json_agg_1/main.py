best_car = None
min_cost = None
for car in cars:
        if min_cost is None or car["cost"] < min_cost:
                min_cost = car["cost"]
                best_car = car
if best_car:
        print("The best car to buy is:")
        print("Name:", best_car["name"])
else:
        print("No cars available to choose from.")
