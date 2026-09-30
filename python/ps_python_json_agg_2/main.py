best_laptop = laptops[0]
min_price, max_battery = best_laptop["price"], best_laptop["battery_life"]
for laptop in laptops[1:]:
        price, battery = laptop["price"], laptop["battery_life"]
        if price < min_price or (price == min_price and battery > max_battery):
                min_price, max_battery, best_laptop = price, battery, laptop
print("The best laptop to buy is:")
print("Name:", best_laptop["name"])
